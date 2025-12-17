import numpy as np
import scipy.signal
import librosa
import librosa.display
import matplotlib.pyplot as plt

# 1.Test
sr = 44100
# A. White Noise
y_white = np.random.randn(int(sr * 2.0)).astype(np.float32)
# B. impluse 신호
y_impulse = np.zeros(1024, dtype=np.float32)
y_impulse[100] = 1.0

# 2. Filter (Low-pass 16kHz)
cutoff_hz = 16000
sos = scipy.signal.butter(6, cutoff_hz, btype="lowpass", fs=sr, output="sos")

# 3. Filter 적용 비교
# Causal
y_bad_spec = scipy.signal.sosfilt(sos, y_white)
y_bad_time = scipy.signal.sosfilt(sos, y_impulse)

# Zero-phase Fileter
y_good_spec = scipy.signal.sosfiltfilt(sos, y_white)
y_good_time = scipy.signal.sosfiltfilt(sos, y_impulse)

# 4. 시각화 1: 스펙트로그램 (주파수가 잘렸는가?)
fig, ax = plt.subplots(nrows=2, figsize=(10, 6), sharex=True)
D_bad = librosa.amplitude_to_db(np.abs(librosa.stft(y_bad_spec)), ref=np.max)
librosa.display.specshow(D_bad, sr=sr, x_axis='time', y_axis='linear', ax=ax[0])
ax[0].set_title("Standard Filter (sosfilter) - Frequency cut OK")

D_good = librosa.amplitude_to_db(np.abs(librosa.stft(y_good_spec)), ref=np.max)
librosa.display.specshow(D_good, sr=sr, x_axis='time', y_axis='linear', ax=ax[1])
ax[1].set_title("Zero-phase Filter (sosfiltfilt) - Frequency Cut OK")
plt.tight_layout()
plt.show()

# 5. 시각화 2: 파형 비교 (시간이 밀렸는가?)
plt.figure(figsize=(10, 4))
# 원본 위치 (검은 점선)
plt.plot(y_impulse[:200], label='Original Impulse', color='black', linestyle='--')
# 일반 필터 (빨간색) -> 오른쪽으로 밀림!
plt.plot(y_bad_time[:200], label='sosfilt (Delayed)', color='red', alpha=0.7)
# Zero-phase 필터 (초록색) -> 원본과 정확히 일치!
plt.plot(y_good_time[:200], label='sosfiltfilt (Aligned)', color='green', alpha=0.7)

plt.title("Phase Shift Check: Impulse Response")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()