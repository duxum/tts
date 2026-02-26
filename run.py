import argparse
from pathlib import Path
import time
import scipy.io.wavfile
from transformers import pipeline

model_id = "duxum/mms-tts-kin"


def generate(text, output):
    output_dir = Path.cwd() / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / (f"{output}.wav" if output != None else "audio.wav")

    print("Loading model.")
    synthesiser = pipeline("text-to-speech", model=model_id)

    print("Generating speech.")
    start = time.time()
    speech = synthesiser(text)
    end = time.time()
    print(f"Generated in {(end - start):.3f} seconds")

    print("Saving speech")
    scipy.io.wavfile.write(
        output_file, rate=speech["sampling_rate"], data=speech["audio"][0]
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate speech from text from Kinyarwanda."
    )

    parser.add_argument("text", type=str, help="Text to speak")

    parser.add_argument(
        "--output", type=str, default=None, help="Optional output audio filename"
    )

    args = parser.parse_args()

    generate(args.text, args.output)

    print("Done!")


if __name__ == "__main__":
    main()
