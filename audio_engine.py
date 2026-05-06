import sounddevice as sd
import numpy as np
import librosa

# -------------------------
# CONFIG
# -------------------------
SAMPLE_RATE = 44100   # ✅ Use supported mic rate
TARGET_SR = 16000     # ✅ For AI models
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
            dtype='float32',
            device=9   # ✅ your working mic device
        )

        sd.wait()

        audio = np.squeeze(audio)

        print("✅ Recording finished")
        print("🔊 Max audio value:", np.max(audio))

        # ✅ Convert to 16kHz (required for Whisper/YAMNet)
        audio = librosa.resample(audio, orig_sr=SAMPLE_RATE, target_sr=TARGET_SR)

        return audio

    except Exception as e:
        print("❌ Mic Error:", e)
        return np.zeros(int(DURATION * TARGET_SR))


# -------------------------
# DEMO AUDIO LOADER
# -------------------------
def load_demo_audio(path):
    print(f"📂 Loading demo audio: {path}")

    try:
        audio, sr = librosa.load(path, sr=TARGET_SR)
        print("✅ Demo audio loaded")
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
