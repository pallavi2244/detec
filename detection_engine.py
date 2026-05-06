import numpy as np

def analyze_context(audio):

    loudness = np.mean(np.abs(audio))

    peak = np.max(np.abs(audio))

    anomaly_score = 0

    abnormal_audio = False

    if loudness > 0.10:

        anomaly_score += 30

    if peak > 0.60:

        anomaly_score += 50

    if anomaly_score >= 50:

        abnormal_audio = True

    return {

        "loudness": float(loudness),

        "peak": float(peak),

        "anomaly_score": anomaly_score,

        "abnormal_audio": abnormal_audio
    }
