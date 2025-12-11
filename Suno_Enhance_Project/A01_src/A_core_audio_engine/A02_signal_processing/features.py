import librosa
import librosa.feature
import numpy as np


def extract_features(y: np.ndarray, sr: int, S: np.ndarray = None, n_fft: int = 2048, hop_length: int = 512) -> dict:
    """
    오디오 신호에서 주요 수치적 특징(RMS, Centroid)을 추출합니다.

    Args:
        y (np.ndarray): 오디오 데이터 (Time domain)
        sr (int): 샘플레이트
        S (np.ndarray, optional): 미리 계산된 Magnitude Spectrogram. (없으면 내부에서 계산)
        n_fft (int): FFT 윈도우 크기
        hop_length (int): 이동 간격

    Returns:
        dict: {
            "rms": np.ndarray (에너지 흐름),
            "centroid": np.ndarray (소리의 밝기/무게중심),
            "times": np.ndarray (시간축)
        }
    """

    # [안전장치 1] 데이터가 비어있으면 빈 딕셔너리나 0으로 채운 결과 반환
    if y.size == 0:
        return {"rms": np.array([]), "centroid": np.array([]), "times": np.array([])}

    # 1. 스펙트로그램 준비 (계산 중복 방지)
    if S is None:
        # y도 없고 S도 없으면 계산 불가 (방어 코드)
        if y is None:
            raise ValueError("y 또는 S 중 하나는 반드시 제공되어야 합니다.")
        S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))

    # 2. 특징 추출
    # S를 넣었으므로 frame_length는 S의 크기에 맞춰 자동 계산되지만, 명시적으로 넣어도 무방함
    rms = librosa.feature.rms(S=S, frame_length=n_fft, hop_length=hop_length)
    cent = librosa.feature.spectral_centroid(S=S, n_fft=n_fft, hop_length=hop_length)

    # 3. 시간축 생성
    times = librosa.times_like(rms, sr=sr, hop_length=hop_length)

    # 4. 결과 반환 (1차원 배열로 변환하여 사용하기 편하게 함)
    return {
        "rms": rms[0],  # (1, T) -> (T,)
        "centroid": cent[0],  # (1, T) -> (T,)
        "times": times
    }