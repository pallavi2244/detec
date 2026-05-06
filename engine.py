from audio_engine import record_audio, load_demo_audio
from detection_engine import detect_distress
from context_engine import analyze_context
from decision_engine import make_decision
from action_engine import trigger_action
from learning_engine import learn_from_event
from utils import print_banner


print_banner()

# -------------------------
# MODE SELECTION
# -------------------------
mode = input("Choose mode (live/demo): ").strip().lower()

if mode not in ["live", "demo"]:
    print("Invalid input, defaulting to LIVE mode")
    mode = "live"

# -------------------------
# MAIN LOOP
# -------------------------
while True:

    print("\n🎧 Listening...")

    # -------------------------
    # INPUT SOURCE
    # -------------------------
    if mode == "demo":
        audio = load_demo_audio("demo_audio/help.wav")
    else:
        audio = record_audio()

    # -------------------------
    # DETECTION
    # -------------------------
    detection_data = detect_distress(audio)

    # -------------------------
    # CONTEXT ANALYSIS
    # -------------------------
    context_data = analyze_context(audio)

    # -------------------------
    # DECISION MAKING
    # -------------------------
    decision = make_decision(detection_data, context_data)

    # -------------------------
    # ACTION
    # -------------------------
    trigger_action(audio, decision)

    # -------------------------
    # LEARNING
    # -------------------------
    learn_from_event(decision)

    # -------------------------
    # OUTPUT
    # -------------------------
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

    print("\n🚦 ALERT LEVEL:")
    print(decision["alert_level"])
