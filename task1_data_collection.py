import requests
import json
import os
import time
from datetime import datetime as dt
# Function to fetch data from the API

CATEGORY_KEYWORDS = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM",
        "startup", "github", "linux", "developer"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global",
        "policy", "economy", "market", "india",
        "china", "usa", "russia", "minister",
        "court", "law", "trade", "border", "rape", "protest", "refugee", "diplomacy", "sanction", "nuclear", "cyber", "espionage"
    ],

    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game",
        "team", "player", "league", "championship",
        "match", "cup", "cricket", "football",
        "tennis", "goal", "win", "tournament",
        "final", "score","coach", "athlete","olympics", "baseball", "hockey", "golf"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome",
        "lab", "scientist", "mars", "moon",
        "earth", "quantum", "energy", "climate"
    ],

    "entertainment": [
        "movie", "film", "music", "Netflix",
        "game", "book", "show", "award", "streaming",
        "series", "video", "TV", "youtube"
    ]
}

response = requests.get(
    "https://hacker-news.firebaseio.com/v0/topstories.json",
    headers={"User-Agent": "TrendPulse/1.0"},
    timeout=10
)

if response.status_code == 200:
    top_ids = response.json()[:500]
else:
    print("Failed to fetch top stories")
    top_ids = []


all_stories = []

counts= {"technology": 0, "worldnews": 0, "sports": 0, "science": 0, "entertainment": 0}

for story_id in top_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story = requests.get(url, headers={"User-Agent": "TrendPulse/1.0"}).json()
    title = story.get("title", "")

    found_category = None
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower()in title.lower():
                found_category = category
               
                break
        if found_category:
            break
    if found_category and counts[found_category] < 25 :
        clean_story = {
            "post_id": story["id"],
            "title": title,
            "category": found_category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": dt.now().isoformat()
        }
        all_stories.append(clean_story)
        counts[found_category] += 1

# Save the collected stories to a JSON file
time.sleep(2)  # To avoid hitting API rate limits
os.makedirs("data", exist_ok=True)

today = dt.now().strftime("%Y-%m-%d")
filename = f"data/trends_{today}.json"

with open(filename, "w") as file:
    json.dump(all_stories, file, indent=4)

print(counts)
print(f"Collected {len(all_stories)} stories. Saved to {filename}") 


    