import os
import soundfile as sf
import datetime
import requests


def print_banner():
    print("\n🚀 AI DISTRESS SYSTEM\n")


def save_audio(audio):

    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    filename = f"recordings/alert_{datetime.datetime.now().strftime('%H%M%S')}.wav"

    sf.write(filename, audio, 16000)

    print(f"💾 Saved: {filename}")


def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return f"{data.get('city')}, {data.get('region')}, {data.get('country')}"
    except:
        return "Unknown location"
