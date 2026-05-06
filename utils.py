import scipy.io.wavfile as wav
import time

def save_audio(audio):
    filename = f"recording/{time.time()}.wav"
    wav.write(filename, 16000, (audio * 32767).astype("int16"))
