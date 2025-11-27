import sys
import numpy as np
import librosa
import soundfile as sf
from pathlib import Path

def load_audio(input_path : str, target_sr: int = 44100, mono: bool = True):
    p = Path(input_path)
    # 1. 파일 존재 여부 검사
    if not p.exists():
        print(f"File '{input_path}' does not exist")
        sys.exit(1)
    # 2. 확장자 검사 (***수정됨: .lower() 적용***)
    # 확장자를 소문자로 변환하여 .WAV, .MP3도 허용합니다.
    suffix_lower = p.suffix.lower()
    if not (suffix_lower== ".wav" or suffix_lower == ".mp3"):
        print(f"File '{input_path}' has unsupported suffix '{p.suffix}'")
        sys.exit(1)

    try:
        # 3. Librosa 로드 (mono=mono로 수정하여 유연성 확보)
        print(f"Loading audio from '{input_path}'")
        y, sr = librosa.load(p, sr=target_sr, mono=mono)
        # 4. Duration Guard Check (300초 = 5분)
        duration = librosa.get_duration(y=y, sr=sr)
        if duration > 300:
            raise Exception(f"Audio duration is too long ({duration:.2f}s)")
        # 5. 최종 반환
        return y, sr, duration

    except Exception as e:
        # 파일 손상, 코덱 문제 등 예상치 못한 오류 처리
        print(f"Failed to load audio from '{e}'")
        sys.exit(1)

def save_audio(output_path: str, data: np.ndarray, sr: int = 44100, subtype: str = 'PCM_16'):
    """
    오디오 데이터를 지정된 포맷으로 안전하게 파일에 저장합니다.

    Args:
        output_path (str): 저장할 파일의 경로 (예: 'outputs/result.wav')
        data (np.ndarray): 저장할 오디오 데이터 (float32, 범위 -1.0 ~ 1.0)
        sr (int): 샘플레이트 (기본값 44100)
        subtype (str): 저장 포맷 (기본값 'PCM_16', 고음질 'FLOAT')
    """
    p = Path(output_path)

    # 1. 데이터 유효성 검사 (빈 데이터 방지)
    # numpy 배열은 .size로 검사하는 것이 더 명확합니다.
    if data is None or data.size == 0:
        print(" Error: 저장할 오디오 데이터가 없습니다 (Empty Data).")
        sys.exit(1)

    # 2. 데이터 클리핑 방지 (안전장치)
    # 1.0을 초과하는 값을 잘라내어 소리가 찢어지는 것을 방지합니다.
    data_safe = np.clip(data, -1.0, 1.0)

    try:
        # 3. [Robustness] 부모 폴더 자동 생성
        # 저장할 폴더가 없으면 미리 생성합니다.
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            print(f" 폴더가 생성되었습니다: '{p.parent}'")

        # 4. 파일 쓰기 수행
        print(f" Saving audio to '{p.name}'...")
        sf.write(file=str(p), data=data_safe, samplerate=sr, subtype=subtype)

        # 5. 저장 확인
        if p.exists():
            print(f"성공: 파일이 정상적으로 저장되었습니다.")

    except Exception as e:
        # 권한 문제, 디스크 용량 부족 등 런타임 오류 처리
        print(f" 오류 발생: 파일 저장에 실패했습니다.\n   오류 내용: {e}")
        sys.exit(1)