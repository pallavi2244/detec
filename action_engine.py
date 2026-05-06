import random

def get_location():
    lat = 12.97 + random.uniform(-0.01, 0.01)
    lon = 77.59 + random.uniform(-0.01, 0.01)
    return f"https://maps.google.com/?q={lat},{lon}"

def act(level, category, score):

    print("CATEGORY:", category)

    if level in ["HIGH", "CRITICAL"]:
        print("📍 Location:", get_location())

    if level == "CRITICAL":
        print("🚨 CALL POLICE")

    elif level == "HIGH":
        print("🚑 SEND ALERT")

    elif level == "MEDIUM":
        print("⚠️ LOG EVENT")
