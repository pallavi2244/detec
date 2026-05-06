from audio_engine import record_audio, load_demo_audio
from detection_engine import detect_distress
from context_engine import analyze_context
from decision_engine import make_decision
from action_engine import trigger_action
from learning_engine import learn_from_event
from utils import print_banner

print_banner()

# ✅ ADD MODE SELECTION
mode = input("Choose mode (live/demo): ").strip().lower()

while True:

    print("\nListening...")

    # ✅ FIXED INPUT HANDLING
    if mode == "demo":
        audio = load_demo_audio("demo_audio/help.wav")
    else:
        audio = record_audio()

    # Detection
    detection_data = detect_distress(audio)

    # Context
    context_data = analyze_context(audio)

    # Decision
    decision = make_decision(detection_data, context_data)

    # Action
    trigger_action(audio, decision)

    # Learning
    learn_from_event(decision)

    # Output
    print("\nTRANSCRIPT:")
    print(detection_data["transcript"])

    print("\nPANIC WORDS:")
    print(detection_data["panic_words"])

    print("\nDETECTED SOUND:")
    print(detection_data["detected_sound"])

    print("\nCONFIDENCE:")
    print(round(detection_data["sound_confidence"], 2))

    print("\nLOUDNESS:")
    print(round(context_data["loudness"], 2))

    print("\nTHREAT SCORE:")
    print(decision["threat_score"])

    print("\nALERT LEVEL:")
    print(decision["alert_level"])
