import os
import scipy.io.wavfile as wav
import time

def save_audio(audio):

    # ✅ AUTO-CREATE FOLDER
    if not os.path.exists("recording"):
        os.makedirs("recording")

    filename = f"recording/{time.time()}.wav"

    wav.write(
        filename,
        16000,
        (audio * 32767).astype("int16")
    )

def print_banner():
    print("=" * 60)
    print(" AI DISTRESS DETECTION SYSTEM ")
    print("=" * 60)
