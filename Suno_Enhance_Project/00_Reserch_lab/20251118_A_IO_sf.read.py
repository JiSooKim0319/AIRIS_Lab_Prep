import soundfile as sf
from pathlib import Path

# 2) sf.read()`의 기본 문법 (가장 중요)**
# 읽어올 파일 경로
file_path = Path("my_audio.wav") # pathlib과 호환가능.

try:
    # 1. 파일 읽기 시도
    # data 변수에는 오디오 파형이, samplerate 변수에는 샘플레이트가 저장됩니다.
    data, samplerate = sf.read(file_path)

    # 2. 정보 출력
    print(f"File: {file_path}")
    print(f"Samplerate: {samplerate} Hz")
    print(f"Shape: {data.shape}")
    print(f"dtype: {data.dtype}")

except Exception as e:
    print(f"Error: {e}")
