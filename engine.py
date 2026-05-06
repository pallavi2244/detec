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
    ("Medical", "I can't breathe call ambulance"),
    ("Fire", "Fire and smoke everywhere"),
    ("Violence", "Help someone grabbing me"),
    ("Mentally Disturbed", "I feel unsafe and scared"),
    ("Accident", "Huge crash help needed")
]

# -------------------------
# MODE SELECTION
# -------------------------
mode = input("Choose mode (demo/live): ").strip().lower()

if mode not in ["demo", "live"]:
    print("Invalid input, defaulting to DEMO mode")
    mode = "demo"


# -------------------------
# DEMO MODE
# -------------------------
if mode == "demo":
    print("\n🧠 Running DEMO (text scenarios)...")

    for label, text in DEMO_SCENARIOS:
        print(f"\n--- {label} ---")

        fake_audio = np.ones(16000 * 3) * (0.5 if label != "Safe" else 0.1)

        detection_data = {
            "transcript": text,
            "panic_words": [],
            "detected_sound": "simulated",
            "sound_confidence": 0.8,
            "distress_detected": False if label == "Safe" else True
        }

        context_data = {
            "loudness": np.max(fake_audio),
            "abnormal_audio": False if label == "Safe" else True
        }

        decision = make_decision(detection_data, context_data)

        # 🔥 Needed for emergency logic
        decision["transcript"] = text

        trigger_action(fake_audio, decision)
        learn_from_event(decision)

        print("\n📜 TEXT:", text)
        print("⚠️ THREAT SCORE:", decision["threat_score"])
        print("🚨 ALERT LEVEL:", decision["alert_level"])

        time.sleep(2)


# -------------------------
# LIVE MODE (VOICE EXIT + AUTO CALL)
# -------------------------
else:
    print("\n🎤 Running LIVE microphone mode...")
    print("👉 Say 'exit' to stop\n")

    while True:
        print("\n🎧 Listening...")

        audio = record_audio()

        detection_data = detect_distress(audio)
        context_data = analyze_context(audio)
        decision = make_decision(detection_data, context_data)

        # 🔥 Needed for emergency logic
        decision["transcript"] = detection_data["transcript"]

        trigger_action(audio, decision)
        learn_from_event(decision)

        transcript = detection_data["transcript"].lower()

        print("\n📜 TRANSCRIPT:", transcript)
        print("⚠️ THREAT SCORE:", decision["threat_score"])
        print("🚨 ALERT LEVEL:", decision["alert_level"])

        # 🔥 VOICE EXIT
        if "exit" in transcript:
            print("\n👋 Ending live demo...")
            break
