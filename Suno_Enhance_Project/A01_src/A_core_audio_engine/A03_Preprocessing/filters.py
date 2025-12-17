import numpy as np
import scipy.signal


def apply_dc_offset_removal(y: np.ndarray) -> np.ndarray:
    """
    신호의 평균을 0으로 맞추어 DC Offset을 제거합니다.
    """
    if y.size == 0:
        return y

    mean_val = np.mean(y)

    if not np.isfinite(mean_val):
        return y

    return y - mean_val


def apply_normalize(y: np.ndarray, target_level: float = 0.95) -> np.ndarray:
    """
    오디오의 최대 피크를 target_level로 맞춥니다 (Peak Normalization).
    """
    peak = np.max(np.abs(y))

    if peak < 1e-9:
        return y

    return y / peak * target_level


def _create_sos_filter(filter_type: str, cutoff_hz: float, sr: int, order: int = 6) -> np.ndarray:
    """
    [내부 함수] Butterworth 필터의 계수(SOS)를 생성합니다.
    """
    # Nyquist 주파수 안전장치
    nyquist = sr / 2
    if cutoff_hz >= nyquist:
        cutoff_hz = nyquist - 1.0

    sos = scipy.signal.butter(
        N=order,
        Wn=cutoff_hz,
        btype=filter_type,
        fs=sr,
        output='sos'
    )

    return sos


def apply_filter(y: np.ndarray, sos: np.ndarray) -> np.ndarray:
    """
    [공통 함수] 생성된 필터 계수(sos)를 사용하여 오디오에 필터를 적용합니다.
    (Zero-phase filtering: 위상 지연 없음)
    """
    if y.size == 0:
        return y

    if not np.all(np.isfinite(y)):
        return y

    # Zero-phase 필터링 적용 (filtfilt)
    y_filtered = scipy.signal.sosfiltfilt(sos, y)

    return y_filtered.astype(np.float32)


def apply_lowpass_filter(y: np.ndarray, cutoff_hz: float, sr: int, order: int = 6) -> np.ndarray:
    """
    특정 주파수 이상을 제거합니다 (고음 노이즈 제거용).
    """
    # 1. 필터 설계도(sos) 만들기
    sos = _create_sos_filter('lowpass', cutoff_hz, sr, order)

    # 2. 필터 적용하기
    return apply_filter(y, sos)


def apply_highpass_filter(y: np.ndarray, cutoff_hz: float, sr: int, order: int = 6) -> np.ndarray:
    """
    특정 주파수 이하를 제거합니다 (저음 웅웅거림/Hum 제거용).
    """
    # 1. 필터 설계도(sos) 만들기
    sos = _create_sos_filter('highpass', cutoff_hz, sr, order)

    # 2. 필터 적용하기
    return apply_filter(y, sos)