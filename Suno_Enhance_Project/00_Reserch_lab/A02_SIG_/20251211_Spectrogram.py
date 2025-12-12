import numpy as np
import librosa
import librosa.feature
import librosa.display
import matplotlib.pyplot as plt
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. (Load -> stft -> abs -> Amplitude)
y, sr, duration = load_audio("../test_input.wav")
D = librosa.stft(y, n_fft=2048, hop_length=512)
S = np.abs(D)
S_dB = librosa.amplitude_to_db(S, ref=np.max)

# 2. Feature Extraction
rms = librosa.feature.rms(S=S, frame_length=2048, hop_length=512)
cent = librosa.feature.spectral_centroid(S=S, n_fft=2048, hop_length=512)

# 3. Visualization (pyplot -> DisPlay.specshow -> plt.savefig)
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10, 8))

# --- [첫째 칸] ---
img = librosa.display.specshow(S_dB, x_axis='time', y_axis='hz',
                               sr=sr, hop_length=512,
                               ax=ax[0], cmap="magma")
# colorbar
fig.colorbar(img, ax=ax[0], format='%+2.0f dB')
ax[0].set_title('Spectrogram & Spectral Centroid')

# centroid 겹쳐 그리기
times = librosa.times_like(cent, sr=sr, hop_length=512)
ax[0].plot(times, cent[0], label="Spectral Centroid",color='w', linewidth=2)
ax[0].legend(loc="upper right")
# --- [두쨰 칸] ---

ax[1].plot(times, rms[0], color="r", label="RMS Energy",linewidth=2)
ax[1].set_title("RMS Energy")
ax[1].set_xlabel("Time (s)")
ax[1].legend(loc="upper right")

# 4. 마무리 및 저장
plt.tight_layout()

# 따옴표 위치 수정 & 확장자 추가
fig.savefig("output_spectrogram.png", dpi=150, bbox_inches='tight')

print(" 시각화 완료 및 저장됨 ")
plt.show()