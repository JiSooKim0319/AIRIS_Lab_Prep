import numpy as np

def apply_dc_offset_removal(y: np.ndarray) -> np.ndarray:
    """
    Applies the DC offset removal filter to the given signal.
    """
    # 1. 빈 데이터 방어 (Empty Array Check)
    if y.size == 0:
        return

    # 2. 평균값 계산
    mean_val = np.mean(y)

    # 3. NaN/Inf 방어 (비정상 데이터가 들어올 경우 원본 반환)
    if not np.isfinite(mean_val):
        return y
    # 4. Dc offset 제거
    return y - mean_val

def apply_normalize(y : np.ndarray, target_level : float = 0.95) -> np.ndarray:
    """
    Applies the normalization filter to the given signal.
    """

    # 1. peak 찾기
    peak = np.max(np.abs(y))

    # 2. 무음 이거나 매우 작은 것 처리
    if peak < 1e-9:
        return y

    # 3. 비율 계산 및 적용
    return y / peak * target_level
