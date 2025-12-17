import sys
import numpy as np
import librosa
import soundfile as sf
from pathlib import Path


def load_audio(input_path: str, target_sr: int = 44100, mono: bool = True):
    p = Path(input_path)

    # 1. 파일 존재 여부 검사
    if not p.exists():
        raise FileNotFoundError(f"File '{input_path}' does not exist")

    # 2. 확장자 검사
    suffix_lower = p.suffix.lower()
    if suffix_lower not in [".wav", ".mp3", ".flac", ".m4a"]:  # FLAC, M4A 추가
        raise ValueError(f"File '{input_path}' has unsupported suffix '{p.suffix}'")

    try:
        print(f"📂 Loading audio from '{p.name}'...")
        y, sr = librosa.load(p, sr=target_sr, mono=mono)

        # 4. Duration Guard Check (300초 = 5분)
        duration = librosa.get_duration(y=y, sr=sr)
        if duration > 300:
            raise ValueError(f"Audio duration is too long ({duration:.2f}s)")

        return y, sr, duration

    except Exception as e:
        print(f"❌ Failed to load audio: {e}")
        # 여기서 sys.exit() 대신 빈 배열을 반환하거나 에러를 다시 던집니다.
        # 자동화 파이프라인을 위해 빈 배열과 0을 반환하여 멈추지 않게 합니다.
        return np.array([]), target_sr, 0.0


def save_audio(output_path: str, data: np.ndarray, sr: int = 44100, subtype: str = 'PCM_16'):
    p = Path(output_path)

    # 1. 데이터 유효성 검사
    if data is None or data.size == 0:
        print("⚠️ Error: 저장할 데이터가 비어있습니다.")
        return  # 강제 종료 대신 함수만 종료

    # 2. 클리핑 방지
    data_safe = np.clip(data, -1.0, 1.0)

    try:
        # 3. 부모 폴더 생성
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)

        # 4. 저장
        print(f"💾 Saving to '{p.name}'...")
        sf.write(file=str(p), data=data_safe, samplerate=sr, subtype=subtype)

    except Exception as e:
        print(f"❌ Save failed: {e}")
        # 저장 실패는 치명적일 수 있으니 로그만 남기고 넘어갑니다.