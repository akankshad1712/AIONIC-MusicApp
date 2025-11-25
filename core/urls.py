# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('generate/', views.generate_music, name='generate_music'), 
    path('history/', views.history, name='history'),
    path('spotify/', views.spotify_recommendations, name='spotify_recommendations'),

    path('profile/', views.profile, name='profile'),
   path('logout/', views.logout_view, name='logout_view')



]
