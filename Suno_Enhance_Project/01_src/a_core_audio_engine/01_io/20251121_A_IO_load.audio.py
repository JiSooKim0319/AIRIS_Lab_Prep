import sys
import numpy as np
import librosa
from pathlib import Path

def load_audio(input_path : str, target_sr: int = 44100, mono: bool = True):
    p = Path(input_path)
    if not p.exists():
        print(f"File '{input_path}' does not exist")
        sys.exit(1)

    if not (p.suffix == ".wav" or p.suffix == ".mp3"):
        print(f"File '{p.suffix}' is not a .wav or .mp3 file")
        sys.exit(1)

    try:
        print(f"Loading audio from '{input_path}'")
        y, sr = librosa.load(p, sr=target_sr, mono=True)
        duration = librosa.get_duration(y=y, sr=sr)
        if duration > 300:
            raise Exception(f"Audio duration is too long ({duration:.2f}s)")

        return y, sr, duration

    except Exception as e:
        print(f"Failed to load audio from '{e}'")
        sys.exit(1)
