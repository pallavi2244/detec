import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
DURATION = 2

def get_audio():
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1,
                   dtype='float32')
    sd.wait()
    return np.squeeze(audio)
