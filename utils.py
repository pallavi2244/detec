import os
import numpy as np
import soundfile as sf
import datetime
import requests


# -------------------------
# BANNER
# -------------------------
def print_banner():
    print("\n==============================")
    print("🚀 AI DISTRESS DETECTION SYSTEM")
    print("==============================\n")


# -------------------------
# SAVE AUDIO
# -------------------------
def save_audio(audio):

    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    filename = f"recordings/alert_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

    sf.write(filename, audio, 16000)

    print(f"💾 Audio saved: {filename}")


# -------------------------
# GET LOCATION
# -------------------------
def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()

        city = data.get("city", "")
        region = data.get("region", "")
        country = data.get("country", "")

        return f"{city}, {region}, {country}"

    except:
        return "Location not available"
