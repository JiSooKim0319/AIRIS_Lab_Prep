import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# 1. 파라미터 설정
sr = 44100
cutoff_hz = 16000  # 16kHz 이상을 제거 (Low-pass)
order = 6          # 필터의 가파른 정도 (기울기)

# 2. 필터 설계
# fs=sr: 정규화 주파수 대신 사람이 쓰는 Hz 단위를 직접 입력 가능
# output="sos": 수치적 안정성을 위해 필수 설정
sos = scipy.signal.butter(N=order, Wn=cutoff_hz, btype="lowpass", fs=sr, output="sos")
    # N = order : 주파수 경사 (소리 왜곡 정함)
    # Wn = cutoff_hz = 어디서 부터 자를 지 경계선 지정

print(f"sos 계수 형태 : {sos.shape}")

# 3. 주파수 응답 계산 (검증용)
# 설계된 필터가 실제로 주파수를 어떻게 깎는지 계산
freqs, response = scipy.signal.sosfreqz(sos, fs=sr)

# 4. 시각화
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(freqs, 20 * np.log10(np.abs(response)))

ax.set_title(f"Butterworth low-pass Filter ({cutoff_hz} Hz, Order={order})")
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Amplitude [dB]")

# 컷오프 지점 표시 (-3dB 지점이 컷 오프여야 함)
ax.axvline(cutoff_hz, color='red', linestyle='--', label='Cutoff Frequency')
ax.axhline(-3, color='gray', linestyle=':', label='-3dB Point')

# 그래프 보기 좋게 설정
ax.set_ylim(-80, 5) # -80dB 밑으로는 안 보이게
ax.grid(True)
ax.legend()
plt.show()
