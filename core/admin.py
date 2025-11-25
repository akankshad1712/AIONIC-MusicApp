# core/admin.py
from django.contrib import admin
from .models import Profile, Generation

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob')

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ('user','prompt','duration_seconds','mood','created_at')
    readonly_fields = ('created_at',)
