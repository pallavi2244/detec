from audio_engine import record_audio
from detection_engine import detect_distress
from context_engine import analyze_context
from decision_engine import make_decision
from action_engine import trigger_action
from learning_engine import learn_from_event
from utils import print_banner

import numpy as np
import time


print_banner()

# -------------------------
# DEMO SCENARIOS
# -------------------------
DEMO_SCENARIOS = [
    ("Safe", "Hey how are you"),
    ("Medical", "I can't breathe"),
    ("Fire", "Fire in building"),
    ("Violence", "Help someone attacking me"),
    ("Hindi", "bachao koi mujhe pakad raha hai"),
    ("Kannada", "sahay madi yaro nanna hidididdare"),
    ("Multi Emergency", "fire and i am kidnapped")
]

# -------------------------
# MODE SELECTION
# -------------------------
mode = input("Choose mode (demo/live): ").strip().lower()

if mode not in ["demo", "live"]:
    mode = "demo"


# -------------------------
# DEMO MODE
# -------------------------
if mode == "demo":
    print("\n🧠 Running DEMO...")

    for label, text in DEMO_SCENARIOS:
        print(f"\n--- {label} ---")

        fake_audio = np.ones(16000 * 3) * 0.5

        detection_data = {
            "transcript": text,
            "panic_words": [],
            "detected_sound": "simulated",
            "sound_confidence": 0.8,
            "distress_detected": True
        }

        context_data = {
            "loudness": 0.5,
            "abnormal_audio": True
        }

        decision = make_decision(detection_data, context_data)

        decision["transcript"] = text

        trigger_action(fake_audio, decision)

        print("TEXT:", text)
        print("ALERT:", decision["alert_level"])

        time.sleep(2)


# -------------------------
# LIVE MODE
# -------------------------
else:
    print("\n🎤 LIVE MODE STARTED")
    print("👉 Say 'end call' to stop\n")

    while True:
        print("\n🎧 Listening...")

        audio = record_audio()

        detection_data = detect_distress(audio)
        context_data = analyze_context(audio)
        decision = make_decision(detection_data, context_data)

        decision["transcript"] = detection_data["transcript"]

        trigger_action(audio, decision)

        transcript = detection_data["transcript"].lower()

        print("\nTRANSCRIPT:", transcript)
        print("ALERT:", decision["alert_level"])

        if "end call" in transcript:
            print("👋 Ending demo...")
            break
