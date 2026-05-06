from utils import save_audio

def trigger_action(audio, decision):

    if decision["threat_score"] >= 60:

        save_audio(audio)

        print("\nEMERGENCY AUDIO SAVED")

        with open("incident_log.txt", "a") as f:
            f.write(
                f"{decision['alert_level']} | {decision['threat_score']}\n"
            )
