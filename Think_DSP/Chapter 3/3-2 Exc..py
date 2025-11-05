import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write  # WAV 저장

# 1) 공통 파라미터
fs = 44100
T = 4.0
f0 = 440.0
octaves = 3
f1 = f0 * (2 ** octaves)
amp = 0.9

t = np.linspace(0, T, int(fs*T), endpoint=False)

# 2) 선형 처프
k = (f1 - f0) / T
phase_lin = 2*np.pi * (f0*t + 0.5*k*t**2)
y_lin = amp * np.cos(phase_lin).astype(np.float32)

# 3) 지수 처프
alpha = np.log(f1/f0) / T
phase_exp = 2*np.pi * f0 * (np.exp(alpha*t) - 1.0) / alpha
y_exp = amp * np.cos(phase_exp).astype(np.float32)

# 4) 파형 비교 플롯 (앞부분 확대)
plt.figure(figsize=(10,4))  # ← figsize 오타 수정
N = 2000
plt.plot(t[:N], y_lin[:N], label="Linear")
plt.plot(t[:N], y_exp[:N], label="Exponential", alpha=0.8)
plt.title("Waveforms (first {} samples)".format(N))  # ← 공백 추가
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()
plt.show()

# 5) 스펙트로그램 비교
plt.figure(figsize=(10,7))  # ← figsize 오타 수정
plt.subplot(2,1,1)
plt.specgram(y_lin, NFFT=2048, Fs=fs, noverlap=1024, cmap="magma")
plt.title("Spectrogram - Linear chirp")
plt.ylabel("Frequency (Hz)")

plt.subplot(2,1,2)
plt.specgram(y_exp, NFFT=2048, Fs=fs, noverlap=1024, cmap="magma")
plt.title("Spectrogram - Exponential chirp")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()

# 6) WAV 저장 (int16 변환)
y_lin_i16 = (y_lin * 32767).astype(np.int16)
y_exp_i16 = (y_exp * 32767).astype(np.int16)
write("OutPut/chirp_linear_440_to_3oct.wav", fs, y_lin_i16)
write("OutPut/chirp_exponential_440_to_3oct.wav", fs, y_exp_i16)
print("Saved:", os.path.abspath("OutPut/chirp_linear_440_to_3oct.wav"))
print("Saved:", os.path.abspath("OutPut/chirp_exponential_440_to_3oct.wav"))

# 7) 간단 재생 (플랫폼별)
def play(path):
    if sys.platform == "darwin":      # macOS
        os.system(f"afplay '{path}'")  # ← 따옴표 중복 제거
    elif os.name == "nt":             # Windows
        os.system(f'start "" "{path}"')  # ← 표준 형태
    else:
        # Linux: aplay(alsa) 또는 xdg-open 중 선택
        if os.system(f"aplay '{path}'") != 0:
            os.system(f"xdg-open '{path}'")

print("Playing Linear...")
play("OutPut/chirp_linear_440_to_3oct.wav")
print("Playing Exponential...")
play("OutPut/chirp_exponential_440_to_3oct.wav")
