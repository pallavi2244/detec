from utils import save_audio, get_location

def trigger_action(audio, decision):

    transcript = decision.get("transcript", "").lower()
    score = decision.get("threat_score", 0)

    print("DEBUG transcript:", transcript)   # 🔍 helps debugging

    # 🔥 LOWER THRESHOLD FOR DEMO
    if score >= 30:

        save_audio(audio)
        location = get_location()

        services = []

        # -------------------------
        # FIRE
        # -------------------------
        if any(word in transcript for word in ["fire", "smoke", "burn"]):
            services.append(("🔥 Fire Department", "101"))

        # -------------------------
        # MEDICAL
        # -------------------------
        if any(word in transcript for word in ["breathe", "ambulance", "faint", "pain"]):
            services.append(("🚑 Ambulance", "102"))

        # -------------------------
        # POLICE (FIXED KEYWORDS)
        # -------------------------
        if any(word in transcript for word in [
            "help", "attack", "attacking", "danger",
            "grab", "kidnap", "kidnapped", "threat", "assault"
        ]):
            services.append(("👮 Police", "100"))

        # fallback
        if not services:
            services.append(("🚨 Emergency", "112"))

        # -------------------------
        # OUTPUT
        # -------------------------
        print("\n🚨 EMERGENCY DETECTED!")

        for service, number in services:
            print(f"📞 Calling {service} ({number})")

        print(f"📍 Location sent: {location}")

        # -------------------------
        # SAVE LOG
        # -------------------------
        with open("incident_log.txt", "a", encoding="utf-8") as f:
            for service, number in services:
                f.write(
                    f"{decision['alert_level']} | {score} | {service} | {location}\n"
                )
