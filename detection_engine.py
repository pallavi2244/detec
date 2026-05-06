import numpy as np
import librosa

def detect_scream(audio):
    return min(np.abs(audio).mean() * 3, 1.0)

def get_loudness(audio):
    return np.abs(audio).mean()

def detect_pitch(audio):
    pitches, mags = librosa.piptrack(y=audio, sr=16000)
    vals = pitches[mags > 0]
    return vals.mean() if len(vals) > 0 else 0

def pitch_stress(p):
    if p > 300:
        return 1
    elif p > 200:
        return 0.5
    return 0

def detect_stutter(text):
    words = text.split()
    return sum(1 for i in range(1, len(words)) if words[i] == words[i-1])

def voice_instability(audio):
    return np.abs(audio[1:] - audio[:-1]).mean()

def ai_risk(scream, loud, stress, stutter):
    return min((scream*0.4 + loud*0.2 + stress*0.3 + min(stutter,2)*0.1)*100, 100)
