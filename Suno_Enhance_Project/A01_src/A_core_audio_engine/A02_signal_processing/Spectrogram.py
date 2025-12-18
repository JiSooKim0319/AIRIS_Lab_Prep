import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from typing import Optional, Tuple, Dict


# [수정 1] from os import times <-- 삭제함 (충돌 원인)

def compute_stft_db(y: np.ndarray, n_fft: int = 2048, hop_length: int = 512) -> Tuple[np.ndarray, np.ndarray]:
    """
    오디오 신호를 스펙트로그램으로 변환합니다.
    (안전장치: NaN/Inf 데이터가 들어오면 0으로 치환하여 에러 방지)
    """
    if y is None or y.size == 0:
        return np.array([]), np.array([])

    # 데이터 무결성 체크
    if not np.all(np.isfinite(y)):
        y = np.nan_to_num(y)

    # 1. STFT -> Magnitude
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))

    # 2. Magnitude -> dB (ref=max: 최대값을 0dB로)
    S_dB = librosa.amplitude_to_db(S, ref=np.max)

    return S_dB, S


def plot_spectrogram(
        S_dB: np.ndarray,
        sr: int,
        output_path: str,
        hop_length: int = 512,
        title: str = "Audio Analysis",
        features: Optional[Dict[str, np.ndarray]] = None
):
    """
    스펙트로그램 위에 Rolloff, Centroid, 16kHz 기준선을 겹쳐 그려서 저장.

    Args:
        S_dB: compute_stft_db의 결과 (dB 스케일)
        sr: 샘플레이트
        output_path: 저장할 이미지 경로 (.png)
        features: features.py 결과 딕셔너리 (times, rolloff, centroid 등)
    """

    # 1. 데이터 유효성 검사
    if S_dB is None or S_dB.size == 0:
        return

    # 2. 캔버스 준비
    has_rms = (features is not None
               and "rms" in features
               and isinstance(features["rms"], np.ndarray)
               and features["rms"].size > 0)

    nrows = 2 if has_rms else 1

    # sharex=True: 시간축 공유
    fig, ax = plt.subplots(nrows=nrows, sharex=True, figsize=(10, 8 if has_rms else 5))

    if nrows == 1:
        ax = [ax]

    # [수정 2] times 변수 안전하게 추출 (None 방지)
    times = features.get("times") if features else None

    # --- Spectrogram (Main) ----
    # y_axis='linear': 16kHz 절단을 확인하기 위해 선형 축 사용
    img = librosa.display.specshow(S_dB, x_axis="time", y_axis="linear",
                                   ax=ax[0], hop_length=hop_length, sr=sr, cmap="inferno")

    fig.colorbar(img, ax=ax[0], format="%+2.0f dB")
    ax[0].set_title(f"{title} - Spectrogram")

    # [Guide 1] 16kHz 기준선 (Nyquist 고려)
    if sr > 32000:
        ax[0].axhline(y=16000, color='r', linestyle='--', alpha=0.5, label='16kHz Threshold')

    # [Guide 2] Feature Overlay (겹쳐 그리기)
    if times is not None and times.size > 0:
        if "rolloff" in features and features["rolloff"].size == times.size:
            ax[0].plot(times, features["rolloff"], label="Rolloff", color='w', linewidth=1.5)

        if "centroid" in features and features["centroid"].size == times.size:
            ax[0].plot(times, features["centroid"], label="Centroid", color='cyan', linewidth=1, alpha=0.8)

    ax[0].legend(loc="upper right", fontsize='small')

    # --- RMS Energy (Sub) ---
    if has_rms:
        # RMS 정규화
        rms = features["rms"]
        rms_norm = rms / (np.max(rms) + 1e-6)

        # [수정 3] times가 유효한지 한 번 더 확인 후 plot
        if times is not None and times.size == rms.size:
            ax[1].plot(times, rms_norm, color="orange", label="Normalized RMS")
            ax[1].set_title("RMS Energy")
            ax[1].set_ylabel("Amplitude")
            ax[1].legend(loc="upper right")

    # --- 저장 및 메모리 정리 ---
    plt.tight_layout()
    try:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    except Exception as e:
        print(f"Plotting failed: {e}")
    finally:
        plt.close()