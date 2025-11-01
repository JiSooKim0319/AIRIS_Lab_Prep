# filename: spectrogram_numpy_demo_annotated.py
# 목표:
# - 1초 길이의 선형 처프 신호(220 Hz → 440 Hz)를 생성한다.
# - 단시간 푸리에 변환(STFT)으로 스펙트로그램을 계산한다.
# - 스펙트로그램(0~700 Hz)과 원 신호 파형을 위/아래 두 개의 서브플롯으로 시각화한다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft  # STFT 계산을 위한 함수

# 1) 신호(선형 처프) 만들기 ------------------------------------------------------
fs = 11025            # 샘플레이트(Hz). 1초에 몇 개의 샘플을 찍을지 결정. 11.025 kHz는 가벼운 예제에 적절
T = 1.0               # 신호 길이(초). 1초짜리 신호를 만든다
t = np.linspace(      # 시간축 벡터 생성: 0초부터 T초 직전까지 균일한 간격으로 샘플 생성
    0, T, int(fs*T), endpoint=False
)

f0, f1 = 220.0, 440.0 # 시작 주파수 220 Hz, 끝 주파수 440 Hz
k = (f1 - f0) / T     # 선형 처프의 주파수 변화율(Hz/s). 1초 동안 220 Hz만큼 증가

# 선형 처프의 위상 식:
# θ(t) = 2π [ f0 * t + (1/2) * k * t^2 ]
# 주파수 f(t)가 f0 + k t이므로, 위상은 주파수의 시간 적분으로 얻는다.
phase = 2*np.pi * (f0*t + 0.5*k*t**2)

# 코사인으로 실제 신호 y(t) 생성. float32는 오디오/시각화에 충분하고 메모리 절약에도 유리
x = np.cos(phase).astype(np.float32)

# 2) STFT로 스펙트로그램 만들기 ---------------------------------------------------
# STFT 핵심 파라미터:
# - nperseg: 창 길이(프레임 길이). 길수록 주파수 해상도↑, 시간 해상도↓
# - noverlap: 프레임 간 겹침 샘플 수. 보통 50~75%가 무난
# - window: 창 함수(Hann, Hamming 등). 새는 스펙트럼 에너지를 줄여 깔끔한 피크를 도와줌
nperseg = 512
noverlap = nperseg // 2        # 50% 겹침
win = np.hanning(nperseg)      # 해밍/한을 주로 사용. 여기서는 Hann 창

# stft는 복소수 행렬 Zxx와 그에 대응하는 주파수 벡터 f(Hz), 시간 벡터 tt(초)를 반환
# - Zxx.shape = (주파수빈 수, 시간프레임 수)
f, tt, Zxx = stft(
    x, fs=fs, window=win, nperseg=nperseg, noverlap=noverlap, boundary=None
)

# 복소수 STFT의 크기(magnitude)를 취해 스펙트로그램의 “세기”를 만든다
S = np.abs(Zxx)

# 3) 700 Hz 이하만 잘라 보기(저역만 확대하여 처프 증가가 더 선명하게 보이도록) -------
high = 700
# 주파수 벡터 f 중 high 이하인 인덱스만 선택. 비교 연산 후 where로 인덱스 얻기
hi_idx = np.where(f <= high)[0]

# 시각화에 쓸 주파수축(f_plot)과 해당 대역만 잘라낸 스펙트로그램(S_plot)
f_plot = f[hi_idx]
S_plot = S[hi_idx, :]

# 4) 시각화 -----------------------------------------------------------------------
plt.figure(figsize=(10, 6))  # 전체 그림 크기

# (윗그림) 스펙트로그램: 시간 vs 주파수 vs 에너지
plt.subplot(2, 1, 1)

# dB 스케일로 변환: 20*log10(|S|). 아주 작은 값은 로그에서 -inf가 되지 않게 바닥값을 둔다
S_db = 20 * np.log10(np.maximum(S_plot, 1e-10))

# pcolormesh로 컬러 맵 그리기
# - x축: 시간(tt), y축: 주파수(f_plot), 색: dB 값(S_db)
# - shading="gouraud"는 렌더링을 부드럽게
plt.pcolormesh(tt, f_plot, S_db, shading="gouraud", cmap="magma")

plt.title("Spectrogram (STFT, 0–700 Hz)")  # 제목
plt.ylabel("Frequency (Hz)")               # y축 라벨
cbar = plt.colorbar()                      # 색상바(크기 기준)
cbar.set_label("Magnitude (dB)")           # 색상바 라벨

# (아랫그림) 원 신호 파형
plt.subplot(2, 1, 2)
plt.plot(t, x)                             # 시간-진폭 파형
plt.title("Waveform (Linear Chirp 220 → 440 Hz)")
plt.xlabel("Time (s)")                     # x축 라벨
plt.ylabel("Amplitude")                    # y축 라벨(진폭이므로 dB 아님)

plt.tight_layout()                         # 서브플롯 간격 자동 조정
plt.show()
