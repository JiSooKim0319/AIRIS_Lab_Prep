import librosa
import numpy as np


def apply_hpss(y: np.ndarray, margin: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """
    오디오를 Harmonic(멜로디)과 Percussive(타격음) 성분으로 분리합니다.

    Args:
        margin (float or tuple): 분리 경계의 엄격함.
            - float: 두 성분에 동일한 마진 적용 (기본 1.0)
            - tuple: (harmonic_margin, percussive_margin) 형태로 개별 적용 가능
    """
    # 1. 빈 데이터 방어
    if y.size == 0:
        return y, y

    # 2. NaN/Inf 방어
    if not np.all(np.isfinite(y)):
        return y, y

    # 3. HPSS 분리 수행
    try:
        y_harmonic, y_percussive = librosa.effects.hpss(y, margin=margin)
        return y_harmonic, y_percussive
    except Exception as e:
        print(f"❌ HPSS failed: {e}")
        return y, np.zeros_like(y)  # 실패 시 원본과 무음을 반환
