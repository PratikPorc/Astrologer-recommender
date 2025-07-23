import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_astrology_advice(input_text):
    prompt = f"""You are a wise and compassionate astrologer. A user has provided the following palm reading or horoscope summary:

"{input_text}"

Based on this, give a short but deep life insight or piece of spiritual advice.
"""

    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",  # Free on Together.ai
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 0.9,
        "prompt": prompt
    }

    response = requests.post("https://api.together.xyz/v1/completions", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

palm_reading_1 = "The mount of Saturn is raised, and the heart line is long and deep."
horoscope_summary_1 = "The birth chart shows Rahu in the 1st house and Venus in the 7th."

print("🖐️ Palm Reading Insight:\n", get_astrology_advice(palm_reading_1))
print("\n🌌 Horoscope Insight:\n", get_astrology_advice(horoscope_summary_1))
