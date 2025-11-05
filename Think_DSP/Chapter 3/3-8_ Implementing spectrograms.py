# filenmae : tmplementing_spectrograms.py
# 목표 :
# - 스펙트로그램을 '직접' 구현한다 ( 프레이밍 -> 윈도윙 -> FFT -> dB -> 시각화).
# - 선형 처프 신호(220->440 Hz)를 예제로 사용한다.

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1) 예제 신호: 선형 처프 생성
# ------------------------------------------------------------
fs = 11025                      # 샘플레이트(Hz). 1초당 샘플 수
T = 1.0                         # 신호 길이(초)
t = np.linspace(0, T, int(fs*T), endpoint=False)  # 0~T 직전까지 균일 샘플

f0, f1 = 220.0, 440.0           # 시작/끝 주파수(Hz)
k = (f1 - f0) / T               # 선형 처프의 주파수 변화율(Hz/s)
# 위상 θ(t)=2π(f0 t + ½ k t^2). 주파수 f(t)=f0 + k t 를 적분해서 얻음.
phase = 2*np.pi*(f0*t + 0.5*k*t**2)
x = np.cos(phase).astype(np.float32)   # 실제 신호(코사인). float32로 메모리 절약

# ------------------------------------------------------------
# 2) STFT 파라미터 설정
# ------------------------------------------------------------
nperseg = 512                # 창 길이(프레임 길이). 길수록 주파수↑ 시간↓
noverlap = nperseg // 2         # 오버랩(50%). 연결 매끄럽게, 정보 손실↓
hop = nperseg - noverlap        # 프레임 간 이동량(샘플 수)
win = np.hanning(nperseg)       # Hann 창: 경계 부드럽게(누출 감소)

# 총 프레임 수 계산: 마지막 불완전 프레임은 버림
num_frames = 1 + (len(x) - nperseg) // hop
# 양수 주파수만 표시(실수 FFT의 절반+1 크기)
freqs = np.fft.rfftfreq(nperseg, d=1/fs)     # 크리 : nperseg//2 + 1
# 스펙트럼 크기 행렬을 미리 할당: [주파수빈, 프레임]
S_mag = np.empty((len(freqs), num_frames), dtype=np.float32)

# ------------------------------------------------------------
# 3) 프레이밍→윈도잉→FFT→크기 계산 루프
# ------------------------------------------------------------
for i in range(num_frames):
    start = i * hop                          # 이번 프레임 시작 인덱스
    frame = x[start:start+nperseg]           # 길이 nperseg 조각
    frame_win = frame * win                  # 창 곱하기(경계 급변 완화)
    X = np.fft.rfft(frame_win)               # 양수 주파수만 FFT(복소수)
    S_mag[:, i] = np.abs(X)                  # 크기 스펙트럼 저장
# ------------------------------------------------------------
# 4) 크기를 dB로 변환(시각 대비 향상)
# ------------------------------------------------------------
# 로그 전 0 방지를 위해 아주 작은 값으로 바닥을 깔아준다.
S_db = 20 * np.log10(np.maximum(S_mag, 1e-10))

# ------------------------------------------------------------
# 5) 시간축(각 프레임의 '중심' 시각) 만들기
# ------------------------------------------------------------
# 프레임 i의 중심은 시작시각 + nperseg/2 샘플 만큼 지난 지점
times = (np.arange(num_frames) * hop + nperseg/2) / fs

# ------------------------------------------------------------
# 6) 시각화(0~700 Hz만 확대)
# ------------------------------------------------------------
f_high = 700
mask = freqs <= f_high

plt.figure(figsize=(10,6))


# 위 = 스펙트로그램
plt.subplot(2,1,1)
# pcolormesh(X=시간, Y=주파수, C=크기(dB))
plt.pcolormesh(times, freqs[mask], S_db[mask, : ], shading="gouraud", cmap="magma")
plt.title("Spectrogram (SFTF, 0-700 Hz)  ")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
cbar = plt.colorbar()
cbar.set_label("Magnitude (dB)")

# 아래 : 원 신호 파형
plt.subplot(2,1,2)
plt.plot(t, x, color="gray")
plt.title("Waveform (Linear Chirp 220 -> 440 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 7) 추가 학습 포인트(메시지)
# ------------------------------------------------------------
print("- 학습 포인트 -")
print("• 창 길이(nperseg)를 늘리면 주파수 분해능↑, 시간 해상도↓ (가보르 한계).")
print("• Hann 같은 창을 곱으면 누출(leakage)이 줄어 스펙트럼이 깔끔해집니다.")
print("• noverlap(50~75%)로 프레임을 촘촘히 하면 시간 변화가 더 매끄럽게 보입니다.")
print("• dB 스케일은 작은 신호도 보이게 하고 시각 대비를 높여줍니다.")























