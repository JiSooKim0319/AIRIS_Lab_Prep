import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def compute_spectrogram(y: np.ndarray, n_fft: int = 2048, hop_length: int = 512) -> tuple:
    """
    Audio -> dB Spectrogram 변환
    """
    D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    S = np.abs(D)
    S_dB = librosa.amplitude_to_db(S, ref=np.max)
    return S_dB, S


def save_analysis_plot(
        S_dB: np.ndarray,
        rms: np.ndarray,
        cent: np.ndarray,
        times: np.ndarray,
        sr: int,
        output_path: str,
        title: str = "Audio Analysis",  # <-- 여기가 핵심! 제목을 밖에서 받아옵니다.
        hop_length: int = 512
):
    """
    [자동화 핵심] 스펙트로그램, Centroid, RMS를 한 장의 이미지로 그려서 저장합니다.
    매번 코드를 칠 필요 없이 이 함수만 호출하면 됩니다.
    """
    # 1. 캔버스 준비 (2단)
    fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10, 8))

    # --- [첫째 칸: 스펙트로그램 + 센트로이드] ---
    img = librosa.display.specshow(S_dB, x_axis='time', y_axis='hz',
                                   sr=sr, hop_length=hop_length,
                                   ax=ax[0], cmap="magma")
    fig.colorbar(img, ax=ax[0], format='%+2.0f dB')

    # 제목 설정 (인자로 받은 title 사용)
    ax[0].set_title(f'{title} - Spectrogram & Centroid')

    # Centroid 겹쳐 그리기
    ax[0].plot(times, cent, label="Spectral Centroid", color='w', linewidth=2)
    ax[0].legend(loc="upper right")

    # --- [둘째 칸: RMS 에너지] ---
    ax[1].plot(times, rms, color="r", label="RMS Energy", linewidth=2)
    ax[1].set_title('RMS Energy')
    ax[1].set_xlabel('Time (s)')
    ax[1].legend(loc="upper right")

    # 2. 저장 및 종료
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()  # 메모리 해제 (필수)

    print(f"✅ Analysis saved to: {output_path}")