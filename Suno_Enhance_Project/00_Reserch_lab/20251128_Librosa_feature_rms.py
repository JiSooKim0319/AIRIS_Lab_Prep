import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. 데이터 로드
y, sr , duration = load_audio('test_input.wav')

# 2. RMS 에너지 계산 (핵심)
frame_length = 2048
hop_length = 512 # STFT와 동일하게 설정하여 시간축 정렬

# center = True는 Librosa의 기본값이며, 프레임 중심을 시간축에 맞춥니다.
rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length, center=True)

# 3. 시각화 ( 파형 vs 에너지 바교)
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10,4))

# 아래쪽 : RMS 에너지 (빨간 선) - 시간축을 맞추기 위해 times_like 사용
# times_likes는 RMS 배열의 프레임 개수에 맞춰 정확한 시간 축을 생성함
times = librosa.times_like(rms, sr=sr, hop_length=hop_length)
ax[1].plot(times, rms[0], color="r", label="RMS Energy")
ax[1].set(title="RMS (Energy)", xlabel="Time (s)")

# 위쪽 : 원본 파형
librosa.display.waveshow(times, sr=sr, ax=ax[0], alpha=0.5)
ax[0].set(title="Waveform")
ax[0].label_outer() # 상위 Axes의 X축 라벨을 제거하여 깔끔하게 만든다.

fig.tight_layout()
plt.show() # 자동화에서는 fig.savefig + plt.close(fig) 사용