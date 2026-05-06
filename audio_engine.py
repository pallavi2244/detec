import sounddevice as sd
import numpy as np
import librosa

SAMPLE_RATE = 16000
DURATION = 3


def record_audio():
    print("🎤 Recording started... Speak now")

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
    try:
        audio, sr = librosa.load(path, sr=SAMPLE_RATE)
        return audio
    except Exception as e:
        print("❌ Demo load error:", e)
        return np.zeros(int(DURATION * SAMPLE_RATE))
