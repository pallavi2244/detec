import sounddevice as sd
import numpy as np
import whisper
import librosa
import time
import random
import scipy.io.wavfile as wav

# ================= CONFIG =================
SAMPLE_RATE = 16000
DURATION = 2
DEMO_MODE = True

# ================= MODEL =================
model = whisper.load_model("base")

# ================= PANIC WORDS =================
PANIC_WORDS = set(["help", "stop", "save me", "ambulance", "fire"])

# ================= CONTEXT =================
context_scores = []

# ================= DEMO =================
DEMO_SCENARIOS = [
    ("Safe", "Hey, can you grab groceries?"),
    ("Medical", "I can't breathe, call an ambulance!"),
    ("Fire", "There's fire and smoke everywhere!"),
    ("Violence", "Help! Someone is grabbing me!"),
    ("Mental", "I don’t want to be here anymore"),
    ("Accident", "Huge crash, people need help!")
]

# ================= AUDIO =================
def get_audio():
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1,
                   dtype='float32')
    sd.wait()
    return np.squeeze(audio)

# ================= DETECTION =================
def speech_to_text(audio):
    wav.write("temp.wav", SAMPLE_RATE, (audio * 32767).astype("int16"))
    return model.transcribe("temp.wav")["text"]

def detect_scream(audio):
    return min(np.abs(audio).mean() * 3, 1.0)

def get_loudness(audio):
    return np.abs(audio).mean()

def detect_pitch(audio):
    pitches, mags = librosa.piptrack(y=audio, sr=SAMPLE_RATE)
    vals = pitches[mags > 0]
    return vals.mean() if len(vals) > 0 else 0

def pitch_stress(p):
    return 1 if p > 300 else 0.5 if p > 200 else 0

def detect_stutter(text):
    words = text.split()
    return sum(1 for i in range(1, len(words)) if words[i] == words[i-1])

def voice_instability(audio):
    return np.abs(audio[1:] - audio[:-1]).mean()

# ================= AI MODEL =================
def ai_risk(scream, loud, stress, stutter):
    return min((scream*0.4 + loud*0.2 + stress*0.3 + min(stutter,2)*0.1)*100, 100)

# ================= CLASSIFICATION =================
def classify(text):
    t = text.lower()
    if "fire" in t or "smoke" in t: return "FIRE"
    if "breathe" in t or "ambulance" in t: return "MEDICAL"
    if "help" in t or "grab" in t: return "VIOLENCE"
    if "crash" in t: return "ACCIDENT"
    if "don't want" in t: return "MENTAL"
    return "SAFE"

def route(cat):
    return {
        "FIRE": "🔥 FIRE",
        "MEDICAL": "🚑 AMBULANCE",
        "VIOLENCE": "🚓 POLICE",
        "ACCIDENT": "🚨 TRAFFIC",
        "MENTAL": "💬 HELPLINE"
    }.get(cat, "LOG")

# ================= LOCATION =================
def get_location():
    lat = 12.97 + random.uniform(-0.01, 0.01)
    lon = 77.59 + random.uniform(-0.01, 0.01)
    return f"https://maps.google.com/?q={lat},{lon}"

# ================= MAIN =================
def process(text, audio):
    scream = detect_scream(audio)
    loud = get_loudness(audio)
    pitch = detect_pitch(audio)
    stress = pitch_stress(pitch)
    stutter = detect_stutter(text)
    instability = voice_instability(audio)

    # rule score
    score = 0
    for w in PANIC_WORDS:
        if w in text.lower():
            score += 40

    score += scream*50
    if loud > 0.3: score += 20
    if instability > 0.2: score += 15
    if stutter > 1: score += 20

    # AI score
    ai_score = ai_risk(scream, loud, stress, stutter)

    final = min((score*0.6 + ai_score*0.4), 100)

    # context
    context_scores.append(final)
    if len(context_scores) > 5:
        context_scores.pop(0)

    context_sum = sum(context_scores)

    # level
    if context_sum > 200: level = "CRITICAL"
    elif final > 80: level = "HIGH"
    elif final > 40: level = "MEDIUM"
    else: level = "SAFE"

    # learning
    if final > 70:
        for w in text.split():
            if len(w) > 3:
                PANIC_WORDS.add(w.lower())

    category = classify(text)
    service = route(category)

    print("\nTEXT:", text)
    print("SCORE:", round(final,2), "| LEVEL:", level)
    print("CATEGORY:", category)
    print("ACTION:", service)

    if level in ["HIGH","CRITICAL"]:
        print("📍 LOCATION:", get_location())

# ================= RUN =================
print("🚀 AI DISTRESS ENGINE STARTED")

if DEMO_MODE:
    for label, text in DEMO_SCENARIOS:
        print("\n---", label, "---")
        fake_audio = np.ones(16000) * (0.5 if label!="Safe" else 0.1)
        process(text, fake_audio)
        time.sleep(2)

else:
    while True:
        audio = get_audio()
        text = speech_to_text(audio)
        process(text, audio)
