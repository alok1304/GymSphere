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
    generator = pipeline("text-generation", model="gpt2")  # Better model

    prompt = (
        f"Generate a detailed {user_goal} workout plan with warm-up, "
        f"exercises (with sets & reps), rest time, and cooldown."
    )

    result = generator(
        prompt, 
        max_length=200,  
        num_return_sequences=1,  
        temperature=0.5,  # Less randomness
        top_k=40,  
        do_sample=True  
    )

    return result[0]["generated_text"]