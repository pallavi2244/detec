from audio_engine import (
    record_audio,
    load_demo_audio
)

from detection_engine import (
    detect_distress
)

from context_engine import (
    analyze_context
)

from decision_engine import (
    make_decision
)

from action_engine import (
    trigger_action
)

from learning_engine import (
    learn_from_event
)

from utils import (
    print_banner
)

print_banner()

mode = input(
    "\nChoose mode (live/demo): "
)

while True:

    print("\nListening...")

    if mode == "demo":

        audio = load_demo_audio(
            "demo_audio/help.wav"
        )

    else:

        audio = record_audio()

    detection_data = detect_distress(
        audio
    )

    context_data = analyze_context(
        audio
    )

    decision = make_decision(
        detection_data,
        context_data
    )

    trigger_action(
        audio,
        decision
    )

    learn_from_event(
        decision
    )

    print("\nTRANSCRIPT:")
    print(
        detection_data["transcript"]
    )

    print("\nPANIC WORDS:")
    print(
        detection_data["panic_words"]
    )

    print("\nDETECTED SOUND:")
    print(
        detection_data["detected_sound"]
    )

    print("\nCONFIDENCE:")
    print(
        round(
            detection_data[
                "sound_confidence"
            ],
            2
        )
    )

    print("\nLOUDNESS:")
    print(
        round(
            context_data["loudness"],
            2
        )
    )

    print("\nTHREAT SCORE:")
    print(
        decision["threat_score"]
    )

    print("\nALERT LEVEL:")
    print(
        decision["alert_level"]
    )

    print("\nSYSTEM MEMORY UPDATED")
