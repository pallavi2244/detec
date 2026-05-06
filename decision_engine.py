def make_decision(
    detection_data,
    context_data
):

    threat_score = 0

    if detection_data["distress_detected"]:

        threat_score += 50

    threat_score += (
        len(
            detection_data["panic_words"]
        ) * 25
    )

    if context_data["abnormal_audio"]:

        threat_score += 30

    if threat_score >= 90:

        level = "CRITICAL ALERT 🔴"

    elif threat_score >= 60:

        level = "HIGH ALERT 🟠"

    elif threat_score >= 30:

        level = "MEDIUM ALERT 🟡"

    else:

        level = "SAFE 🟢"

    return {

        "threat_score": threat_score,

        "alert_level": level
    }
