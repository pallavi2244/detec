import sounddevice as sd
import numpy as np
import librosa

# -------------------------
# CONFIG
# -------------------------

SAMPLE_RATE = 16000
DURATION = 3   # seconds

# -------------------------
# LIVE AUDIO RECORDING
# -------------------------

def record_audio():
    print("🎤 Recording started... Speak loudly!")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32',
        device=9   # 👈 KEEP THIS (your correct mic)
    )

    sd.wait()

    audio = np.squeeze(audio)

    print("✅ Recording finished")
    print("🔊 Max audio value:", np.max(audio))

    return audio

    except Exception as e:
        print("❌ Error:", e)
        return np.zeros(int(DURATION * SAMPLE_RATE))


# -------------------------
# DEMO AUDIO LOADER
# -------------------------

def load_demo_audio(path):
    print(f"📂 Loading demo audio: {path}")

    try:
        audio, sr = librosa.load(path, sr=SAMPLE_RATE)

        print("✅ Demo audio loaded")

        return audio

    except Exception as e:
        print("❌ Error loading demo audio:", e)
        return np.zeros(int(DURATION * SAMPLE_RATE))


# -------------------------
# OPTIONAL: LIST DEVICES
# -------------------------

def list_devices():
    print("\n🎧 Available Audio Devices:\n")
    print(sd.query_devices())
