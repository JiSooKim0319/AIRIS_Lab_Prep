from A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# 1. 상황 재현: 오프셋 강제 주입 (Suno 음원에 결함이 있다고 가정)
y, sr, _ = load_audio("test_input.wav")
offset_amount = 0.1
y_bad = y + offset_amount

print(f"오프셋 주입 후 평균값: {np.mean(y_bad):.5f}")

# 2. 해결책 A: 단순 평균 차감(Numpy) - Time Domain
# 평균이 0이 아니니, 평균만큼 빼보자
y_fixed_numpy = y_bad - np.mean(y_bad)

# 3. 해결책 B: 선형 추세 제거 (SciPy Detrend) - Frequency/Statistical Domain
# "직선 형태로 기울어진 성분(Trend)을 찾아서 제거하자."
y_fixed_scipy = scipy.signal.detrend(y_bad, type="constant")

# 4. 결과 검증
mean_numpy = np.mean(y_fixed_numpy)
mean_scipy = np.mean(y_fixed_scipy)

# [핵심] 두 방식 모두 0점으로 돌아왔는가?
print(f"NumPy 제거 후 평균값: {mean_numpy:.10f}")
print(f"SciPy 제거 후 평균값: {mean_scipy:.10f}")

# 5. 시각화
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(y_bad[:1000], label="Bad (Offset +0.1)", alpha=0.5, color='red')
ax.plot(y_fixed_numpy[:1000], label="Fixed (Centered)", alpha=0.8, color='green')
ax.axhline(0, color='black', linestyle='--') # 0점 기준선
ax.legend()
ax.set_title("DC Offset Removal: Before vs After")
plt.tight_layout()
plt.show()