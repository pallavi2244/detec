import whisper
import scipy.io.wavfile as wav
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import json
import csv

print("Loading Whisper...")
whisper_model = whisper.load_model("base")

print("Loading YAMNet...")
yamnet_model = hub.load(
    'https://tfhub.dev/google/yamnet/1'
)

class_names = []
class_map_path = "yamnet_class_map.csv"
with open(class_map_path) as csv_file:

    reader = csv.DictReader(csv_file)

    for row in reader:
        class_names.append(row['display_name'])

with open("panic_words.json", "r") as f:

    panic_words = json.load(f)["panic_words"]

def detect_distress(audio):

    wav.write(
        "temp.wav",
        16000,
        (audio * 32767).astype("int16")
    )

    result = whisper_model.transcribe(
        "temp.wav"
    )

    transcript = result["text"].lower()

    detected_words = []

    for word in panic_words:

        if word.lower() in transcript:

            detected_words.append(word)

    waveform = tf.convert_to_tensor(
        audio,
        dtype=tf.float32
    )

    scores, embeddings, spectrogram = yamnet_model(
        waveform
    )

    scores_np = scores.numpy()

    mean_scores = np.mean(scores_np, axis=0)

    top_class = class_names[np.argmax(mean_scores)]

    top_score = np.max(mean_scores)

    distress_sounds = [
        "Scream",
        "Shout",
        "Crying",
        "Yell",
        "Explosion",
        "Gunshot"
    ]

    distress_detected = False

    if any(
        sound.lower() in top_class.lower()
        for sound in distress_sounds
    ):
        distress_detected = True

    return {

        "transcript": transcript,

        "panic_words": detected_words,

        "distress_detected": distress_detected,

        "detected_sound": top_class,

        "sound_confidence": float(top_score)
    }
