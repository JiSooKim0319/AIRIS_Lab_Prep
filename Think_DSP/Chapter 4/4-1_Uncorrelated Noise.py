# filename: uncorrelated_noise_audio_demo.py
# 목표:
# - 440 Hz 톤 + 비상관(백색) 잡음 합성
# - 1) 밴드패스 필터, 2) 스펙트럼 감산으로 잡음 저감
# - 파형/PSD 비교 + 오디오 재생 + WAV 저장

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt, welch, stft, istft
from scipy.io.wavfile import write as wav_write

# 노트북에서 소리 재생(선택)
try:
    from IPython.display import Audio, display
    HAVE_IPY = True
except Exception:
    HAVE_IPY = False

# 재생 유틸(터미널/IDE용, OS별)
import os, sys
def play(path):
    """간단 재생: OS별 기본 플레이어 호출"""
    if sys.platform == "darwin":          # macOS
        os.system(f"afplay '{path}'")
    elif os.name == "nt":                 # Windows
        os.system(f'start "" "{path}"')
    else:                                 # Linux
        if os.system(f"aplay '{path}'") != 0:
            os.system(f"xdg-open '{path}'")

# 1) 신호 생성 ---------------------------------------------------------------
fs = 44100                   # 샘플레이트(Hz)
T  = 2.0                     # 길이(초)
t  = np.linspace(0, T, int(fs*T), endpoint=False)

f0 = 440.0                   # 순수 톤(라 A4)
amp = 0.8
x_tone = amp * np.cos(2*np.pi*f0*t)

# 비상관(백색) 잡음
sigma = 0.25
noise = np.random.normal(0, sigma, size=len(t)).astype(np.float32)

# 합성
y_noisy = x_tone + noise

# 2) 밴드패스 필터 ------------------------------------------------------------
# 440 Hz 주변만 통과하도록 대역 설정(필요에 따라 조절)
lowcut, highcut = 300.0, 600.0
order = 6
sos = butter(order, [lowcut, highcut], btype='band', fs=fs, output='sos')
y_band = sosfiltfilt(sos, y_noisy)  # 위상 왜곡 줄이기 위해 filtfilt

# 3) 스펙트럼 감산 ------------------------------------------------------------
nperseg = 1024
noverlap = nperseg // 2
win = np.hanning(nperseg)

# STFT
f, tt, Zxx = stft(y_noisy, fs=fs, window=win, nperseg=nperseg, noverlap=noverlap, boundary=None)
S = np.abs(Zxx)

# 무성 구간(처음 0.5초)을 잡음 프로파일로 추정
noise_mask = tt < 0.5
noise_profile = np.mean(S[:, noise_mask], axis=1, keepdims=True)

# 감산
alpha = 1.0  # 감산 강도(0.8~1.2에서 조정)
S_denoised = np.maximum(S - alpha*noise_profile, 0.0)

# 위상 유지하여 ISTFT 복원
Zxx_denoised = S_denoised * np.exp(1j*np.angle(Zxx))
_, y_ss = istft(Zxx_denoised, fs=fs, window=win, nperseg=nperseg, noverlap=noverlap, input_onesided=True)
y_ss = y_ss[:len(y_noisy)]

# 4) PSD 비교 -----------------------------------------------------------------
def psd_db(x, fs, nperseg=2048):
    f_psd, Pxx = welch(x, fs=fs, window='hann', nperseg=nperseg, noverlap=nperseg//2)
    Pxx[Pxx == 0] = 1e-20
    return f_psd, 10*np.log10(Pxx)

f_psd, P_noisy = psd_db(y_noisy, fs)
_,     P_band  = psd_db(y_band,  fs)
_,     P_ss    = psd_db(y_ss,    fs)

# 5) 시각화 -------------------------------------------------------------------
plt.figure(figsize=(12, 9))

# (a) 파형(초반 확대)
N_show = 2000
plt.subplot(3, 1, 1)
plt.plot(t[:N_show], y_noisy[:N_show], label='Noisy', alpha=0.7)
plt.plot(t[:N_show], y_band[:N_show],  label='Bandpass', alpha=0.9)
plt.plot(t[:N_show], y_ss[:N_show],    label='SpecSub', alpha=0.9)
plt.title("Waveforms (first {} samples)".format(N_show))
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True, alpha=0.3)

# (b) PSD(0~2 kHz)
plt.subplot(3, 1, 2)
mask = f_psd <= 2000
plt.plot(f_psd[mask], P_noisy[mask], label='Noisy')
plt.plot(f_psd[mask], P_band[mask],  label='Bandpass')
plt.plot(f_psd[mask], P_ss[mask],    label='SpecSub')
plt.axvline(f0, color='k', ls='--', alpha=0.5, label='440 Hz')
plt.title("Power Spectral Density (Welch)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (dB/Hz)")
plt.legend()
plt.grid(True, alpha=0.3)

# (c) 간단 스펙트로그램(필요 시 주석 해제)
# from matplotlib.colors import Normalize
# plt.subplot(3, 1, 3)
# f_stft, tt_stft, Z = stft(y_noisy, fs=fs, window=win, nperseg=nperseg, noverlap=noverlap, boundary=None)
# S_db = 20*np.log10(np.maximum(np.abs(Z), 1e-10))
# plt.pcolormesh(tt_stft, f_stft, S_db, shading='gouraud', cmap='magma', norm=Normalize(vmin=-80, vmax=0))
# plt.ylim(0, 2000); plt.title("Noisy Spectrogram"); plt.xlabel("Time (s)"); plt.ylabel("Hz")

plt.tight_layout()
plt.show()

# 6) 오디오 저장 & 재생 ---------------------------------------------------------
def to_int16(x):
    """클리핑 방지하며 int16로 변환"""
    x = np.asarray(x)
    m = np.max(np.abs(x))
    if m > 1e-9:
        x = x / m * 0.95  # 헤드룸 확보
    return (x * 32767).astype(np.int16)

# 파일로 저장
wav_write("Output/noisy.wav", fs, to_int16(y_noisy))
wav_write("Output/bandpass.wav", fs, to_int16(y_band))
wav_write("Output/specsub.wav", fs, to_int16(y_ss))

print("Saved: noisy.wav, bandpass.wav, specsub.wav")

# 노트북에서 바로 듣기(있으면)
if HAVE_IPY:
    print("Play inline (Notebook):")
    display(Audio(y_noisy, rate=fs))
    display(Audio(y_band,  rate=fs))
    display(Audio(y_ss,    rate=fs))
else:
    # OS 기본 플레이어로 순차 재생
    print("Playing with system player...")
    play("Output/noisy.wav")
    play("Output/bandpass.wav")
    play("Output/specsub.wav")
