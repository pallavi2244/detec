from audio_engine import get_audio
from detection_engine import *
from context_engine import *
from learning_engine import *
from decision_engine import *
from action_engine import act
from utils import save_audio

import numpy as np
import time

DEMO_MODE = True

DEMO_SCENARIOS = [
    ("Safe", "Hey how are you"),
    ("Medical", "I can't breathe call ambulance"),
    ("Fire", "Fire and smoke everywhere"),
    ("Violence", "Help someone grabbing me"),
    ("Mental", "I don't want to live"),
    ("Accident", "Huge crash help needed")
]

print("🚀 AI DISTRESS ENGINE STARTED")

def process(text, audio):

    scream = detect_scream(audio)
    loud = get_loudness(audio)
    pitch = detect_pitch(audio)
    stress = pitch_stress(pitch)
    stutter = detect_stutter(text)
    instability = voice_instability(audio)

    score = calculate_score(text, scream, loud, instability, stutter, PANIC_WORDS)

    ai_score = ai_risk(scream, loud, stress, stutter)

    final = min((score * 0.6 + ai_score * 0.4), 100)

    update_context(final)
    learn(text, final)

    context_score = get_context_score()

    if detect_pattern():
        final += 20

    level = decide(final, context_score)
    category = classify(text)

    print("\nTEXT:", text)
    print("SCORE:", round(final, 2), "| LEVEL:", level)

    if level in ["HIGH", "CRITICAL"]:
        save_audio(audio)

    act(level, category, final)

    save_words()


if DEMO_MODE:

    for label, text in DEMO_SCENARIOS:
        print("\n---", label, "---")
        fake_audio = np.ones(16000) * (0.5 if label != "Safe" else 0.1)
        process(text, fake_audio)
        time.sleep(2)

else:

    while True:
        audio = get_audio()
        text = "help me"  # replace with speech later
        process(text, audio)
