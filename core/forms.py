# core/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# ------------------- REGISTER FORM -------------------
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    dob = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned

# ------------------- AI MUSIC GENERATION FORM -------------------
class MusicGenForm(forms.Form):
    prompt = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Enter prompt for AI music generation...'
        })
    )
    duration_seconds = forms.IntegerField(
        min_value=23,
        max_value=30,
        initial=25,
        widget=forms.NumberInput(attrs={'placeholder': 'Duration in seconds (23-30)'})
    )
