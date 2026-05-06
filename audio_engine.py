import sounddevice as sd
import numpy as np
import librosa

SAMPLE_RATE = 16000
DURATION = 3

def record_audio():

    print("Recording...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32'
    )

    sd.wait()

    return np.squeeze(audio)

def load_demo_audio(path):

    audio, sr = librosa.load(
        path,
        sr=SAMPLE_RATE
    )

    return audio
