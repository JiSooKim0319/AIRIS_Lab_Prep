import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio, save_audio
from IPython.display import Audio, display
import sounddevice as sd  # <-- 새로 추가된 라이브러리
import time               # <-- 재생 대기를 위해 추가

def play_audio(data: np.ndarray, sr: int):
    """
    numpy 배열 형태의 오디오 데이터를 스피커로 재생합니다.
    """
    # 데이터 타입을 float32로 변환 (sounddevice 권장)
    data_float32 = data.astype(np.float32)

    # 재생 시작
    sd.play(data_float32, sr)

    # 재생이 끝날 때까지 대기합니다. (1초에 한 번 체크)
    sd.wait()
# 1. Data Load
y, sr, _ = load_audio("1_Quiet Lights of Christmas_.wav")

# 2. HPSS Separate
duration_seconds = 20
y = y[:sr * duration_seconds]
print(f"테스트를 위해 오디오 길이를 {duration_seconds}초로 단축했습니다.")
y_harmonic, y_percussive = librosa.effects.hpss(y, margin=1)

# 3. Visual
fig, ax = plt.subplots(nrows=3, sharex=True, sharey=True, figsize=(10, 12))


# (1) 원본
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, sr=sr, y_axis='log', x_axis='time', ax=ax[0])
ax[0].set(title='Original Signal (Mixed)')
ax[0].label_outer()

# (2) Harmonic (Melody - 가로줄 위주)
D_h = librosa.amplitude_to_db(np.abs(librosa.stft(y_harmonic)), ref=np.max)
librosa.display.specshow(D_h, sr=sr, y_axis = 'log', x_axis='time', ax=ax[1])
ax[1].set(title="Harmonic Componet (Melody/Vocal)")
ax[1].label_outer()

# (3) Percussive (리듬/노이즈 - 세로줄 위주)
D_p = librosa.amplitude_to_db(np.abs(librosa.stft(y_percussive)), ref=np.max)
librosa.display.specshow(D_p, sr=sr, y_axis='log', x_axis='time', ax=ax[2])
ax[2].set(title='Percussive Component (Rhythm/Noise/Clicks)')

plt.tight_layout()
plt.show()

# 4. 결과 저장
print("💾 분리된 파일 저장 중...")
save_audio("test_input_harmonic1.wav", y_harmonic, sr)
save_audio("test_input_percussive1.wav", y_percussive, sr)
print("✅ 저장 완료. 파일을 재생하여 들어보세요.")

print("\n🎶 Harmonic 트랙 재생 (멜로디 위주):")
display(Audio(filename="test_input_harmonic1.wav"))
print("\n🥁 Percussive 트랙 재생 (리듬 위주):")
display(Audio(filename="test_input_percussive1.wav"))
