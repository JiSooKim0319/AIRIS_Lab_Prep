# filename: leakage_fix_demo.py
# 목적:
# - 단일 톤의 FFT에서 누출(leakage)이 어떻게 보이는지 확인
# - 창 함수(Hann) 적용과 주기 정렬(coherent sampling)로 누출을 줄이는 방법 시연

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq

# 1) 공통 설정 ----------------------------------------------------------
fs = 44100                # 샘플레이트(Hz)
N  = 4096                 # FFT 길이(프레임 길이). 길수록 주파수 분해능↑
t  = np.arange(N) / fs     # 0 ~ (N-1)/fs 시간축

# 2) 테스트 톤 주파수 두 가지 --------------------------------------------
f_bin_exact = 1000.0                        # FFT 빈에 '정렬'되도록 쓸 톤(예시)
# FFT의 빈 간격은 fs/N. 정렬 조건은 f = k * (fs/N) (k는 정수).
# 아래는 일부러 약간 어긋난 주파수(누출이 잘 보임).
f_off = f_bin_exact + 37.3                  # 빈 사이 어긋난 톤

# 3) 신호 생성 -----------------------------------------------------------
x_exact = np.cos(2*np.pi*f_bin_exact*t)     # 빈 정렬 톤
x_off   = np.cos(2*np.pi*f_off*t)           # 빈 어긋난 톤

# 4) 창 함수 준비(누출 완화) ---------------------------------------------
win = np.hanning(N)                         # Hann 창(경계 완화로 사이드로브 감소)
win_gain = np.sum(win)/N                    # 창 이득(진폭 스케일 보정용, 참고)

# 5) FFT 계산 함수 (가독성을 위해 간단 래퍼) ------------------------------
def mag_db(x):
    """실수 신호 x의 양수 주파수 스펙트럼 크기를 dB로 반환"""
    X = rfft(x)                             # 실수 FFT(양의 주파수만)
    mag = np.abs(X) / (N/2)                 # 크기 정규화(대략적 기준)
    mag[mag == 0] = 1e-12                   # 로그 안전장치
    return 20*np.log10(mag)

freqs = rfftfreq(N, 1/fs)                   # 양수 주파수 벡터(Hz)

# 6) 네 가지 경우 스펙트럼 ------------------------------------------------
# (a) 빈 정렬 + 창 없음(직사각)  → 누출 거의 없음
S_exact_rect = mag_db(x_exact)

# (b) 빈 어긋남 + 창 없음        → 누출 큼(옆꼬리 길게 퍼짐)
S_off_rect   = mag_db(x_off)

# (c) 빈 정렬 + Hann 창          → 누출 매우 작음(메인로브 형태만)
S_exact_hann = mag_db(x_exact * win)

# (d) 빈 어긋남 + Hann 창        → 누출 크게 완화(사이드로브 낮음)
S_off_hann   = mag_db(x_off * win)

# 7) 시각화 --------------------------------------------------------------
plt.figure(figsize=(10,8))

#보기 좋은 주파수 범위(0-3000 Hz 제한)
f_max = 3000
mask = freqs <= f_max

plt.subplot(2,1,1)
plt.plot(freqs[mask], S_exact_rect[mask], label='Exact bin, Rect window')
plt.plot(freqs[mask], S_off_rect[mask], label='Offset bin, Rect window')
plt.title("Leakage without window (Rectangular)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2,1,2)
plt.plot(freqs[mask], S_exact_hann[mask], label="Exact bin, Hann window")
plt.plot(freqs[mask], S_off_hann[mask],   label="Off-bin, Hann window", alpha=0.8)
plt.title("Leakage reduced with Hann window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 8) 핵심 정리(출력 메시지) ----------------------------------------------
print("- 핵심 요점 -")
print("1) 빈 정렬(coherent sampling): f = k*(fs/N)에 맞추면 누출이 최소화됩니다.")
print("2) 창 함수(Hann 등): 프레임 경계를 부드럽게 해 사이드로브를 줄여 누출을 완화합니다.")
print("3) 길이 N 증가: 주파수 분해능(빈 간격 fs/N)이 촘촘해져 피크가 더 날카로워 보입니다.")
print("4) 단, 창/길이 선택은 시간-주파수 트레이드오프(가보르 한계)를 고려해 결정하세요.")