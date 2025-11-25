from django.db import models
from django.contrib.auth.models import User

def gen_audio_path(instance, filename):
    return f'generations/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Generation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    duration_seconds = models.PositiveIntegerField(default=25)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=50, blank=True)
    sentiment_score = models.FloatField(null=True, blank=True)
    audio_file = models.FileField(upload_to=gen_audio_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at:%Y-%m-%d %H:%M}'

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
