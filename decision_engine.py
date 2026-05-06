def calculate_score(text, scream, loud, instability, stutter, panic_words):

    score = 0
    text = text.lower()

    for w in panic_words:
        if w in text:
            score += 40

    score += scream * 50

    if loud > 0.3:
        score += 20

    if instability > 0.2:
        score += 15

    if stutter > 1:
        score += 20

    return min(score, 100)


def decide(score, context_score):

    if context_score > 200:
        return "CRITICAL"

    if score > 80:
        return "HIGH"

    if score > 40:
        return "MEDIUM"

    return "SAFE"


def classify(text):

    t = text.lower()

    if "fire" in t or "smoke" in t:
        return "FIRE"

    if "breathe" in t or "ambulance" in t:
        return "MEDICAL"

    if "help" in t or "grab" in t:
        return "VIOLENCE"

    if "crash" in t:
        return "ACCIDENT"

    if "don't want" in t:
        return "MENTAL"

    return "SAFE"


def route(category):

    return {
        "FIRE": "🔥 FIRE",
        "MEDICAL": "🚑 AMBULANCE",
        "VIOLENCE": "🚓 POLICE",
        "ACCIDENT": "🚨 TRAFFIC",
        "MENTAL": "💬 HELPLINE"
    }.get(category, "LOG")
