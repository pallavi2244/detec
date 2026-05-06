import json

try:
    with open("panic_words.json") as f:
        PANIC_WORDS = set(json.load(f))
except:
    PANIC_WORDS = set(["help", "stop", "save me"])

def learn(text, score):
    if score > 70:
        for w in text.split():
            if len(w) > 3:
                PANIC_WORDS.add(w.lower())

def save_words():
    with open("panic_words.json", "w") as f:
        json.dump(list(PANIC_WORDS), f)
