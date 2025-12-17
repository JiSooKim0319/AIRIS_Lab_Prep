import numpy as np
import librosa
from typing import Dict, Any

# todd: 실제 프로젝트 통합 시 아래 주석을 해제하고 프로젝트 로거를 사용하세요.
# from A_Core_Audio_Engine.06_Pipeline_Orchestration_Config_CLI_Artifacts.logger import log_process

def extract_features(y : np.ndarray, sr: int, n_fft  : int = 2048, hop_length : int = 512) -> Dict[str, Any]:
    """
    Args:
        y (np.ndarray): 오디오 데이터 (Time domain)
        sr (int): 샘플레이트
        n_fft (int): FFT 윈도우 크기
        hop_length (int): 이동 간격

    Returns:
        dict: 시각화용 시계열 데이터(arrays)와 판단용 요약 통계(stats) 포함.
              실패 시 표준 Empty Schema 반환.
    """
    def _get_empty_schema(sanitize_flag : float = 0.0):
        return {
            "times" : np.array([]),
            "rms" : np.array([]),
            "centroids" : np.array([]),
            "rolloff" : np.array([]),
            "zcr": np.array([]),
            "stats" : {
                "mean_rms" : 0.0,
                "mean_centroids" : 0.0,
                "mean_rolloff" : 0.0,
                "median_rolloff" : 0.0,
                "mean_zcr" : 0.0,
                "max_zcr" : 0.0,
                "sanitize" : sanitize_flag # [보완] 데이터 오염 여부 플래그 (0:정상, 1:오염됨)
            }
        }

    # 1. 빈 데이터 방어 (y.size)
    if y is None or y.size == 0:
        # log_process("warning", "Skipping feature extraction: Empty audio data")
         return _get_empty_schema()

    # 2. 데이터 무결성 검사 (NaN/Inf 체크)
    sanitized = 0.0
    if not np.all(np.isfinite(y)):
        y = np.nan_to_num(y) # (NaN/Inf)을 0으로 치환
        sanitized = 1.0

    try:
        # 3. STFT 계산
        S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))

        # 4. 4개의 센서

        # (1) RMS (에너지 측정)
        rms = librosa.feature.rms(S=S, hop_length=hop_length)[0]

        # (2) Spectral Centroid (밝기 측정)
        cent = librosa.feature.spectral_centroid(S=S, sr=sr, n_fft=n_fft, hop_length=hop_length) [0]

        # (3) Spectral Rolloff (컷 오프 탐지 - Suno 진단 핵심)
        # 진짜 소리가 존재하는 마지막 한계선
        rolloff = librosa.feature.spectral_rolloff(S=S, sr=sr, n_fft=n_fft, hop_length=hop_length, roll_percent = 0.99) [0]

        # (4) Zero Crossing Rate (노이즈 탐지)
        # 파형이 얼마나 떨리는지 측정하여 금속성 노이즈 찾기
        zcr = librosa.feature.zero_crossing_rate(y, frame_length=n_fft, hop_length=hop_length)[0]

        # 5. 시간 축 생성
        times = librosa.times_like(rms, sr=sr, hop_length=hop_length)

        # 6. 결과 패키징
        return {
            "times" : times,
            "rms" : rms,
            "centroid" : cent,
            "rolloff" : rolloff,
            "zcr" : zcr,

            # [진단용] Analyzer가 한눈에 판단할 요약 수치
            "stats" : {
                "mean_rms" : float(np.mean(rms)),
                "mean_centroid" : float(np.mean(cent)),
                #Rolloff는 평균(Mean)과 중간값(Median)을 같이 봐야 안전.
                "mean_rolloff" : float(np.mean(rolloff)),
                "median_rolloff" : float(np.median(rolloff)),
                # ZCR은 평균(Mean)과 최대값(Max)을 같이 봄
                "mean_zcr" : float(np.mean(zcr)),
                "max_zcr" : float(np.max(zcr)),
                # 데이터 오염 여부 보고
                "sanitize" : sanitized
            }
        }
    except Exception as e:
        print(f"Critical Error in features.py: {e}")
        return _get_empty_schema(sanitize_flag = sanitized)

