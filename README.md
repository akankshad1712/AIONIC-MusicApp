# 🎵 AIONIC – AI-Powered Music Generation & Recommendation Platform

AIONIC is a **full-stack AI-powered music generation and recommendation web application** built using **Django**.  
It analyzes **user mood and sentiment from text input**, generates music accordingly, and provides **Spotify-based playlist recommendations**.

The platform features a **modern admin-style dashboard**, user authentication, history tracking, analytics, and a **game-inspired interactive UI**.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Installation & Setup](#️-installation--setup)
- [Application Routes](#-application-routes)
- [Admin Dashboard Overview](#-admin-dashboard-overview)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Author](#-author)

---

## 📖 Overview

AIONIC enhances music discovery using **emotion-driven AI logic**.  
It combines **AI analysis, analytics dashboards, and modern UI design** to deliver a real-world **SaaS-style music platform** suitable for production-scale applications.

---

## 🚀 Key Features

### 🔐 Authentication & User Management
- User Registration & Login  
- Secure Logout  
- Profile Management  
- Django Authentication System  

### 🎧 AI Music Generator
- Text-based mood detection  
- Automatic sentiment analysis  
- AI-generated music previews  
- Instrument-based music tiles (game-style UI)  

### 🎼 Spotify Recommendations
- Mood-based Spotify playlist suggestions  
- In-app playlist browsing experience  
- Trending playlists display  

### 📊 Dashboard (Admin-Style UI)
- Professional sidebar navigation  
- Dashboard statistics:
  - Total tracks generated  
  - Favorites count  
  - Playlists  
  - Daily streak  
- Trending music section  
- Interactive grid-based music tiles  

### 🕒 History & Favorites
- View previously generated music  
- Save favorite tracks  
- Playlist-style history tracking  

### 🎮 Game-Style UI (Bonus)
- Interactive music tiles (keyboard, saxophone, notes)  
- Music-game inspired visual layout  
- Glassmorphism & gradient UI  

---

## 📸 Screenshots

│── splash.png
<img width="1920" height="1080" alt="Screenshot (811)" src="https://github.com/user-attachments/assets/fb9fbeaf-7e14-4968-b705-706b1f837a46" />

│── Login.png
<img width="1920" height="1080" alt="Screenshot (812)" src="https://github.com/user-attachments/assets/c7a4a869-662f-467f-b727-5a9f141a58a9" />

│── Register.png
<img width="1920" height="1080" alt="Screenshot (813)" src="https://github.com/user-attachments/assets/a0626d5a-bca4-4695-9575-343b8b23e33d" />

│── admin_dashboard.png
<img width="1920" height="1080" alt="Screenshot (814)" src="https://github.com/user-attachments/assets/e244aa10-ed3f-44ab-bc9c-3a014adeba5c" />

│── generator.png
<img width="1920" height="1080" alt="Screenshot (815)" src="https://github.com/user-attachments/assets/c2a5c563-46df-4277-97ca-e61331575aaf" />


## 
│── spotify.png

<img width="1920" height="1080" alt="Screenshot (817)" src="https://github.com/user-attachments/assets/8d3d07d4-6228-4969-b496-095922a72f3b" />
<img width="1920" height="1080" alt="Screenshot (818)" src="https://github.com/user-attachments/assets/2c88a100-5171-49db-a52b-8e917725402d" />
<img width="1920" height="1080" alt="Screenshot (819)" src="https://github.com/user-attachments/assets/7ad71904-82f0-483c-be28-a25f6e0c15ec" />



│── history.png
<img width="1920" height="1080" alt="Screenshot (820)" src="https://github.com/user-attachments/assets/be6471e2-a4e5-4531-ab70-dee1fbffa928" />


│── profile.png
<img width="1920" height="1080" alt="Screenshot (822)" src="https://github.com/user-attachments/assets/b1b43234-a2fa-4821-9293-66e5270bf454" />


## 🛠️ Tech Stack

### Frontend
  HTML5
  CSS3 (Glassmorphism UI)
  JavaScript
 Bootstrap Icons
### Backend
   Django (Python)
   Django Authentication System
   Django Templates

### AI & Logic
  Mood Detection (Rule-based / AI-ready)
  Sentiment Analysis
  Extensible music generation logic
 
### Assets & UI
  Custom Logo: aionic_logo.png
   Responsive Design (Desktop & Laptop)

## 📂 Project Architecture

musicgenn/
│
├── core/
│   ├── templates/
│   │   ├── splash.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── home.html
│   │   ├── admin_dashboard.html
│   │   ├── history.html
│   │   ├── spotify.html
│   │   └── profile.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │       └── aionic_logo.png
│   │
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── manage.py
└── README.md

## 🔗 Application Routes
/               → Splash Page
/login/         → Login Page
/register/      → Register Page
/home/          → User Dashboard
/generate/      → AI Music Generator
/history/       → History Page
/spotify/       → Spotify Recommendations
/profile/       → User Profile
/logout/        → Logout

## 🔮 Future Enhancements

Real AI music generation models

Spotify API authentication integration

Admin analytics with Chart.js

Mobile responsive version

User social sharing features
