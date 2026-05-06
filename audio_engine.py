import sounddevice as sd
import numpy as np
import librosa

SAMPLE_RATE = 16000
DURATION = 3

def record_audio():
    print("🎤 Recording started...")

    try:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='float32',
            device=9
        )

        sd.wait()

        audio = np.squeeze(audio)

        print("✅ Recording finished")
        print("🔊 Max audio value:", np.max(audio))

        return audio

    except Exception as e:
        print("❌ Error:", e)
        return np.zeros(int(DURATION * SAMPLE_RATE))


def load_demo_audio(path):
    audio, sr = librosa.load(path, sr=SAMPLE_RATE)
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
