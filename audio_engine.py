import sounddevice as sd
import numpy as np
import librosa
import os

# -------------------------
# CONFIG
# -------------------------
SAMPLE_RATE = 48000   # Mic recording rate
TARGET_SR = 16000     # For AI models
DURATION = 3          # seconds


# -------------------------
# LIVE AUDIO RECORDING
# -------------------------
def record_audio():
    print("🎤 Recording started... Speak now")

    try:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='float32'
        )

        sd.wait()

        audio = np.squeeze(audio)

        print("✅ Recording finished")
        print("🔊 Max audio value:", np.max(audio))

        # Convert to 16kHz
        audio = librosa.resample(audio, orig_sr=SAMPLE_RATE, target_sr=TARGET_SR)

        return audio

    except Exception as e:
        print("❌ Mic Error:", e)
        return np.zeros(int(DURATION * TARGET_SR))


# -------------------------
# DEMO AUDIO LOADER (FIXED)
# -------------------------
def load_demo_audio(path):
    print(f"📂 Loading demo audio: {path}")

    try:
        # 🔥 Check if file exists
        if not os.path.exists(path):
            print("❌ File NOT found:", path)
            return np.zeros(int(DURATION * TARGET_SR))

        # 🔥 Check if file is empty
        if os.path.getsize(path) == 0:
            print("❌ File is EMPTY (0 KB):", path)
            return np.zeros(int(DURATION * TARGET_SR))

        # 🔥 Load audio
        audio, sr = librosa.load(path, sr=TARGET_SR)

        print("✅ Demo audio loaded successfully")

        return audio

    except Exception as e:
        print("❌ Demo load error:", e)
        return np.zeros(int(DURATION * TARGET_SR))


# -------------------------
# OPTIONAL: LIST DEVICES
# -------------------------
def list_devices():
    print("\n🎧 Available Audio Devices:\n")
    print(sd.query_devices())
