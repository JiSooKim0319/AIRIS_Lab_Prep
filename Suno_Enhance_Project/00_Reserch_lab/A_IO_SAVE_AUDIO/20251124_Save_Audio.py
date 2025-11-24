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
# ================================================================================
def save_audio(output_path : str, data: np.ndarray, sr: int = 44100, subtype='PCM_16'):
    """
        오디오 데이터를 지정된 포맷으로 안전하게 파일에 저장합니다.

        Args:
            output_path (str): 저장할 파일의 경로 (예: 'outputs/result.wav')
            data (np.ndarray): 저장할 오디오 데이터 (float32, 범위 -1.0 ~ 1.0)
            sr (int): 샘플레이트 (예: 44100)
            subtype (str): 저장 포맷 (기본값 'PCM_16', 고음질 'FLOAT')
        """
    p = Path(output_path)

    # 1. 데이터 유효성 검사 (빈 데이터 방지)
    if data is None or len(data) == 0:
        print("Error : Audio data isn't exist")
        sys.exit(1)
    # 2. 데이터 클리핑 방지
    data_safe = np.clip(data,-1.0, 1.0)

    try:
        # 3. [Robustness] 부모 폴더 없을 시 자동 생성
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            print(f" 폴더가 생성되었습니다. '{p.parent}")
        # 4. 파일 쓰기 수행 (들여쓰기 수정됨: if문 밖에서 실행)
        print(f" Saving audio file to '{p}'")
        sf.write(file=str(p), data=data_safe, samplerate=sr, subtype=subtype)
        # 5. 저장 확인
        if p.exists():
            print(f"성공: 파일 '{p.name}'이 정상적으로 저장되었습니다.")

    except Exception as e:
        print(f"오류 발생 : 파일 저장에 실패함. \n 오류 내용 {e}")
        sys.exit(1)










