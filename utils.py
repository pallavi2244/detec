import os
import soundfile as sf
import datetime
import requests


def print_banner():
    print("\n==============================")
    print("🚀 AI DISTRESS DETECTION SYSTEM")
    print("==============================\n")


def save_audio(audio):

    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    filename = f"recordings/alert_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

    sf.write(filename, audio, 16000)

    print(f"💾 Audio saved: {filename}")


def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()

        return f"{data.get('city')}, {data.get('region')}, {data.get('country')}"

    except:
        return "Location not available"
