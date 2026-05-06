import os
import scipy.io.wavfile as wav
import time

def trigger_action(
    audio,
    decision
):

    if decision["threat_score"] >= 60:

        if not os.path.exists("recording"):

            os.makedirs("recording")

        filename = f"recording/{time.time()}.wav"

        wav.write(
            filename,
            16000,
            (audio * 32767).astype("int16")
        )

        print("\nEMERGENCY AUDIO SAVED")

        with open(
            "incident_log.txt",
            "a"
        ) as f:

            f.write(
                f"{time.ctime()} | "
                f"{decision['alert_level']} | "
                f"{decision['threat_score']}\n"
            )
