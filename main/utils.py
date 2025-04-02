import requests
from transformers import pipeline
from dotenv import load_dotenv
import os

# YouTube API
load_dotenv() 
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY") 

def get_youtube_videos(query):
    URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={query}&type=video&key={YOUTUBE_API_KEY}"
    
    response = requests.get(URL)
    data = response.json()
    
    videos = []
    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            videos.append({"title": title, "url": f"https://www.youtube.com/watch?v={video_id}"})
    
    return videos


# Hugging face

def generate_workout_plan(user_goal):
    generator = pipeline("text-generation", model="facebook/opt-1.3b")  # Better model

    prompt = (
        f"Create a structured {user_goal} workout plan including warm-up, "
        f"exercises (sets & reps), rest time, and cooldown."
    )

    result = generator(
        prompt, 
        max_length=300,  # Generate more content
        num_return_sequences=1,  
        temperature=0.7,  # Balanced creativity
        top_k=50,  
        do_sample=True  
    )

    return result[0]["generated_text"]