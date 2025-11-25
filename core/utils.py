import random
from textblob import TextBlob
from pydub import AudioSegment, generators
import io, os

# 1️⃣ Text sentiment
def text_sentiment_score(text):
    tb = TextBlob(text)
    return tb.sentiment.polarity  # -1 .. 1

# 2️⃣ Mood from score
def mood_from_score(score):
    if score > 0.4:
        return "happy"
    if score > 0:
        return "neutral"
    if score <= 0:
        return "sad"

# 3️⃣ Simple AI music generator
def synthesize_audio(prompt, duration_seconds=25, out_path=None):
    seed = abs(hash(prompt)) % 10000
    random.seed(seed)
    base = AudioSegment.silent(duration=duration_seconds*1000)
    for i in range(3):
        freq = random.choice([220, 330, 440, 554, 660]) * (1 + i*0.2)
        amp = random.randint(-12, -4)
        tone = generators.Sine(freq).to_audio_segment(duration=duration_seconds*1000).apply_gain(amp)
        if i == 0:
            seg = tone.pan(-0.5).fade_in(500).fade_out(500)
        elif i ==1:
            seg = tone.pan(0.5).fade_in(400).fade_out(400)
        else:
            seg = tone.pan(0).fade_in(300).fade_out(300)
        base = base.overlay(seg)
    for n in range(4):
        click_freq = random.choice([800,1200])
        click = generators.Sine(click_freq).to_audio_segment(duration=120).apply_gain(-8)
        pos = random.randint(0, max(0, duration_seconds*1000-120))
        base = base.overlay(click, position=pos)
    if out_path:
        base.export(out_path, format='mp3')
        return out_path
    else:
        buf = io.BytesIO()
        base.export(buf, format='mp3')
        return buf.getvalue()

# 4️⃣ Placeholder for image mood detection
def detect_mood_from_image(image_file):
    mood = "happy"
    sentiment_score = 0.8
    confidence = 0.9
    return mood, sentiment_score, confidence
