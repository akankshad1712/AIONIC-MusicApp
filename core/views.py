# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from .models import Profile, Generation, Feedback
from .forms import RegisterForm, MusicGenForm
from .utils import (
    text_sentiment_score,
    mood_from_score,
    synthesize_audio,
    detect_mood_from_image
)
import os, uuid
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ------------------- SPLASH -------------------
def splash(request):
    return render(request, 'splash.html')


# ------------------- LOGIN -------------------
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# ------------------- REGISTER -------------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(data['password'])
            user.save()
            Profile.objects.create(user=user, dob=data.get('dob'))
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# ------------------- DASHBOARD -------------------
@login_required
def home(request):
    return render(request, 'home.html')


# ------------------- AI MUSIC GENERATION -------------------
@login_required
def generate_music(request):
    generation = None

    if request.method == 'POST':
        form = MusicGenForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            duration_seconds = form.cleaned_data['duration_seconds']

            # Auto-detect mood + sentiment
            score = text_sentiment_score(prompt)
            mood = mood_from_score(score)

            # Create DB record
            gen = Generation.objects.create(
                user=request.user,
                prompt=prompt,
                duration_seconds=duration_seconds,
                mood=mood,
                sentiment_score=score
            )

            # Audio output
            filename = f"gen_{request.user.id}_{uuid.uuid4().hex[:10]}.mp3"
            out_dir = os.path.join(settings.MEDIA_ROOT, 'generations', f'user_{request.user.id}')
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, filename)

            synthesize_audio(prompt, duration_seconds, out_path)

            gen.audio_file.name = os.path.relpath(out_path, settings.MEDIA_ROOT)
            gen.save()

            generation = gen
    else:
        form = MusicGenForm()

    return render(request, 'generate.html', {'form': form, 'generation': generation})


# ------------------- HISTORY -------------------
@login_required
def history(request):
    gens = Generation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'generations': gens})


# ------------------- PROFILE -------------------
@login_required
def profile(request):
    return render(request, 'profile.html')

# ------------------- SPOTIFY RECOMMENDATIONS -------------------
@login_required
def spotify_recommendations(request):
    recs = []
    mood = None
    confidence = None
    sentiment_score = None
    prompt = ""
    selected_language = request.POST.get("language", "english")  # default English

    if request.method == "POST":

        # ------------------ 1️⃣ If image uploaded ------------------
        if "image" in request.FILES and request.FILES["image"]:
            uploaded_image = request.FILES["image"]
            mood, sentiment_score, confidence = detect_mood_from_image(uploaded_image)

        # ------------------ 2️⃣ If text prompt ------------------
        else:
            prompt = request.POST.get("prompt", "")
            sentiment_score = text_sentiment_score(prompt)
            mood = mood_from_score(sentiment_score)

        # If mood failed → default
        if not mood:
            mood = "relaxed"

        # ------------------ 3️⃣ Language → Spotify Query Mapping ------------------
        language_queries = {
            "english": f"{mood} mood",
            "hindi": f"{mood} mood hindi music",
            "marathi": f"{mood} marathi songs"
        }

        search_query = language_queries.get(selected_language, f"{mood} mood")

        # ------------------ 4️⃣ Spotify API ------------------
        sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
            )
        )

        try:
            results = sp.search(q=search_query, limit=50, type="track", market="IN")
        except Exception as e:
            print("Spotify API Error:", e)
            results = {"tracks": {"items": []}}

        # ------------------ 5️⃣ Build Recommendations List ------------------
        for item in results["tracks"]["items"]:
            recs.append({
                "name": item["name"],
                "artists": ", ".join([a["name"] for a in item["artists"]]),
                "spotify_embed": f"https://open.spotify.com/embed/track/{item['id']}",
                "album_image": item["album"]["images"][0]["url"] if item["album"]["images"] else None
            })

    # ------------------ Render Page ------------------
    return render(request, "spotify.html", {
        "recs": recs,
        "detected_mood": mood,
        "sentiment_score": sentiment_score,
        "confidence": confidence,
        "selected_language": selected_language,
        "prompt": prompt
    })

# ------------------- LOGOUT -------------------
@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


# -------------------- ADMIN DASHBOARD --------------------
@login_required
def admin_dashboard(request):
    import json

    ai_stats = {
        "labels": json.dumps(["Happy", "Sad", "Relaxed"]),  # chart labels
        "data": json.dumps([10, 15, 7])                    # chart data
    }

    admin_stats = [
        {"title": "Total Users", "count": 120, "bg": "rgba(79,124,255,0.08)"},
        {"title": "Tracks Generated", "count": 250, "bg": "rgba(79,124,255,0.08)"},
        {"title": "Feedback Received", "count": 45, "bg": "rgba(79,124,255,0.08)"}
    ]

    users = request.user.__class__.objects.all()
    feedback_list = Feedback.objects.all()

    return render(request, "home.html", {
        "ai_stats": ai_stats,
        "admin_stats": admin_stats,
        "users": users,
        "feedback_list": feedback_list
    })
