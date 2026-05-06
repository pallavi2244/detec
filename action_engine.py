from utils import save_audio, get_location

def trigger_action(audio, decision):

    transcript = decision.get("transcript", "").lower()
    score = decision.get("threat_score", 0)

    # 🔥 LOWERED THRESHOLD (IMPORTANT FOR LIVE)
    if score >= 30:

        save_audio(audio)

        location = get_location()

        # -------------------------
        # SELECT SERVICE
        # -------------------------
        if any(word in transcript for word in ["fire", "smoke", "burn"]):
            service = "🔥 Fire Department"
            number = "101"

        elif any(word in transcript for word in ["breathe", "ambulance", "faint", "pain"]):
            service = "🚑 Ambulance"
            number = "102"

        elif any(word in transcript for word in ["help", "attack", "danger", "grab", "kidnap"]):
            service = "👮 Police"
            number = "100"

        else:
            service = "🚨 Emergency"
            number = "112"

        # -------------------------
        # OUTPUT (THIS WAS MISSING BEFORE)
        # -------------------------
        print("\n🚨 EMERGENCY DETECTED!")
        print(f"📞 Calling {service} ({number})")
        print(f"📍 Location sent: {location}")

        # -------------------------
        # SAVE LOG
        # -------------------------
        with open("incident_log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{decision['alert_level']} | {score} | {service} | {location}\n"
            )
