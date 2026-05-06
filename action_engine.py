from utils import save_audio, get_location

def trigger_action(audio, decision):

    if decision["threat_score"] >= 60:

        save_audio(audio)

        location = get_location()
        transcript = decision.get("transcript", "").lower()

        # -------------------------
        # SELECT SERVICE
        # -------------------------
        if any(word in transcript for word in ["fire", "smoke"]):
            service = "🔥 Fire Department"
            number = "101"

        elif any(word in transcript for word in ["breathe", "ambulance", "pain"]):
            service = "🚑 Ambulance"
            number = "102"

        elif any(word in transcript for word in ["help", "attack", "danger", "grab"]):
            service = "👮 Police"
            number = "100"

        else:
            service = "🚨 Emergency"
            number = "112"

        # -------------------------
        # ALERT OUTPUT
        # -------------------------
        print("\n🚨 EMERGENCY DETECTED!")
        print(f"📞 Calling {service} ({number})")
        print(f"📍 Location sent: {location}")

        # -------------------------
        # SAVE LOG
        # -------------------------
        with open("incident_log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{decision['alert_level']} | {decision['threat_score']} | {service} | {location}\n"
            )

        # -------------------------
        # SIMULATE CALL
        # -------------------------
        try:
            import os
            os.system(f"start tel:{number}")
        except:
            pass
