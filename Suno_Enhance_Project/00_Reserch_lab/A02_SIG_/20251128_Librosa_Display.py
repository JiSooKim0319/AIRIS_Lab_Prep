import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. 데이터 준비
y, sr , duration = load_audio('../test_input.wav')
D = librosa.stft(y, n_fft = 2048,hop_length=512)
S_dB = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# 2. 캔버스 준비
fig, ax = plt.subplots(figsize=(10, 4))

# 3. 스펙트로그램 그리기 (핵심)
# x_axis = 'time'을 쓰려면 sr과 hop_length를 반드시 넘겨야 합니다.
img = librosa.display.specshow(S_dB, sr=sr, hop_length=512,
                               x_axis="time", y_axis="linear",ax=ax,cmap="magma")

# 4. 컬러바 (범례) 추가
# format="%+2.0f dB" : 숫자를 깔끔하게 표시 (예 : -10dB)
fig.colorbar(img, ax=ax, format='%+2.0f dB')

# 5. 제목 설정 및 출력
ax.set_title("linear Frequency Power Spectrogram")
fig.tight_layout()

# 디버깅용 show (나중엔 savefig로 교체)
plt.show()
