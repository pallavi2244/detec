from audio_engine import record_audio, load_demo_audio
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
# DEMO SCENARIOS (TEXT MODE)
# -------------------------
DEMO_SCENARIOS = [
    ("Safe", "Hey how are you"),
    ("Medical", "I can't breathe call ambulance"),
    ("Fire", "Fire and smoke everywhere"),
    ("Violence", "Help someone grabbing me"),
    ("Mentally Disturbed", "I don't want to live"),
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
# DEMO MODE (TEXT-BASED)
# -------------------------
if mode == "demo":
    print("\n🧠 Running DEMO (text scenarios)...")

    for label, text in DEMO_SCENARIOS:
        print(f"\n--- {label} ---")

        # fake audio (just for pipeline)
        fake_audio = np.ones(16000 * 3) * (0.5 if label != "Safe" else 0.1)

        # simulate detection output
        detection_data = {
            "transcript": text,
            "panic_words": [],
            "detected_sound": "simulated",
            "sound_confidence": 0.8
        }

        context_data = {
            "loudness": np.max(fake_audio)
        }

        decision = make_decision(detection_data, context_data)

        trigger_action(fake_audio, decision)
        learn_from_event(decision)

        print("\n📜 TEXT:", text)
        print("⚠️ THREAT SCORE:", decision["threat_score"])
        print("🚨 ALERT LEVEL:", decision["alert_level"])

        time.sleep(2)


# -------------------------
# LIVE MODE (MIC)
# -------------------------
else:
    print("\n🎤 Running LIVE microphone mode...")

    while True:
        print("\n🎧 Listening...")

        audio = record_audio()

        detection_data = detect_distress(audio)
        context_data = analyze_context(audio)
        decision = make_decision(detection_data, context_data)

        trigger_action(audio, decision)
        learn_from_event(decision)

        print("\n📜 TRANSCRIPT:")
        print(detection_data["transcript"])

        print("\n🚨 PANIC WORDS:")
        print(detection_data["panic_words"])

        print("\n🔊 DETECTED SOUND:")
        print(detection_data["detected_sound"])

        print("\n📊 CONFIDENCE:")
        print(round(detection_data["sound_confidence"], 2))

        print("\n📈 LOUDNESS:")
        print(round(context_data["loudness"], 2))

        print("\n⚠️ THREAT SCORE:")
        print(decision["threat_score"])

        print("\n🚨 ALERT LEVEL:")
        print(decision["alert_level"])
