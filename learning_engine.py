import json
import os

MEMORY_FILE = "memory.json"

if not os.path.exists(MEMORY_FILE):

    with open(MEMORY_FILE, "w") as f:

        json.dump({
            "events": [],
            "average_threat": 0
        }, f)

def learn_from_event(event):

    with open(MEMORY_FILE, "r") as f:

        memory = json.load(f)

    memory["events"].append(event)

    total = 0

    for e in memory["events"]:

        total += e["threat_score"]

    memory["average_threat"] = (
        total / len(memory["events"])
    )

    with open(MEMORY_FILE, "w") as f:

        json.dump(
            memory,
            f,
            indent=4
        )

    print("\nSELF-LEARNING UPDATED")
