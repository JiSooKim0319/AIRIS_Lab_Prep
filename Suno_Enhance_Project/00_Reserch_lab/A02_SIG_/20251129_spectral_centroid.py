import numpy as np
import librosa
import matplotlib.pyplot as plt
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. 데이터 로드
y, sr, _ = load_audio("../test_input.wav")

# 2. Spectral Centroid 계산
# y를 넣으면 내부적으로 STFT를 수행하고 계산합니다.
# sr은 Hz 단위 변환을 위해 필수입니다.
n_fft = 2048
hop_length = 512
cent = librosa.feature.spectral_centroid(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)

# 3. 결과 확인
print(f"Centroid Shape: {cent.shape}")
# 예상: (1, n_frames) -> RMS와 마찬가지로 1줄짜리 데이터

# 4. 시각화 (스펙트로그램 위에 겹쳐 그리기)
S_db = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length)), ref=np.max)

fig, ax = plt.subplots(figsize=(10, 6))
# y_axis='log'를 써야 음악적 직관과 잘 맞습니다.
librosa.display.specshow(S_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log', ax=ax, cmap='magma')
ax.set_title('Spectrogram + Spectral Centroid')

# Centroid 그래프 겹치기 (흰색 선)
times = librosa.times_like(cent, sr=sr, hop_length=hop_length)
ax.plot(times, cent[0], label='Spectral Centroid', color='w', linewidth=2)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()