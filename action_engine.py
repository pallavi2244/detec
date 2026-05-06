from utils import save_audio, get_location

def trigger_action(audio, decision):

    # Only trigger for high threat
    if decision["threat_score"] >= 60:

        save_audio(audio)

        # -------------------------
        # GET DATA
        # -------------------------
        location = get_location()
        transcript = decision.get("transcript", "").lower()

        # -------------------------
        # CHOOSE EMERGENCY SERVICE
        # -------------------------
        if any(word in transcript for word in ["fire", "burn", "smoke"]):
            service = "Fire Department"
            number = "101"

        elif any(word in transcript for word in ["breathe", "ambulance", "faint", "pain"]):
            service = "Ambulance"
            number = "102"

        elif any(word in transcript for word in ["help", "attack", "grab", "danger", "kidnap"]):
            service = "Police"
            number = "100"

        else:
            service = "Emergency Helpline"
            number = "112"

        # -------------------------
        # CREATE ALERT MESSAGE
        # -------------------------
        alert_message = f"""
🚨 EMERGENCY ALERT 🚨
Service: {service} ({number})
Threat Level: {decision['alert_level']}
Score: {decision['threat_score']}
Location: {location}
"""

        # -------------------------
        # DISPLAY ALERT
        # -------------------------
        print(alert_message)

        # -------------------------
        # SAVE LOG
        # -------------------------
        with open("incident_log.txt", "a", encoding="utf-8") as f:
            f.write(alert_message + "\n")

        # -------------------------
        # OPTIONAL: OPEN CALL (SIMULATION)
        # -------------------------
        try:
            import os
            os.system(f"start tel:{number}")   # works on Windows
        except:
            pass
