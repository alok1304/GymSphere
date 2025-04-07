# GymSphere 🏋️‍♂️ – AI-Powered Fitness Platform

GymSphere is a full-stack fitness platform designed to empower users with personalized workout plans, fitness tracking, and seamless access to health content. It integrates AI, APIs, and payment gateways to deliver a complete and modern fitness experience.

## 🚀 Features

- 🔐 **User Authentication**: Secure login, logout, profile settings, and user management.
- 💳 **Stripe Integration**: Real-time pricing updates with secure checkout using Stripe API.
- 📊 **BMI Calculator**: Tracks health metrics and offers insights into body fitness.
- 🎥 **YouTube Data API**: Fetches and displays free workout tutorials dynamically.
- 🧠 **AI-Powered Workout Plans**: Uses Hugging Face Transformers to generate personalized fitness routines based on user goals and preferences.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: Bootstrap, JavaScript
- **Database**: PostgreSQL
- **Payment Gateway**: Stripe API
- **APIs**: Hugging Face Transformers, YouTube Data API
- **Deployment & Tools**: Git


## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alok1304/GymSphere.git
   cd GymSphere
   ```
2. **Create and activate a virtual environment**
   ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**
   Create a `.env` file with your Stripe and API keys:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   ```bash
   STRIPE_API_KEY=your_secret_key
   YOUTUBE_API_KEY=your_youtube_key
   ```
5. **Run the server**
   ```bash
    python manage.py migrate
    python manage.py runserver
   ```       
   
   
   
   
      
   
