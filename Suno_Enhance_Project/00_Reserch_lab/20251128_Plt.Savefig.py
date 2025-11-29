import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
from pathlib import Path
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

y, sr , duration = load_audio('test_input.wav')
D = librosa.stft(y, n_fft=2048, hop_length=512)
s_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

fig, ax = plt.subplots(figsize=(10, 4))
img = librosa.display.specshow(s_db, sr=sr, hop_length=512,ax=ax,x_axis='time', y_axis='linear', cmap="magma")
fig.colorbar(img, ax=ax, format='%+2.0f dB')
ax.set_title("spectrogram Analysis Result")
fig.tight_layout()

#2. 저장 경로 설정 및 폴더 생성
output_dir = Path("artifacts")
output_dir.mkdir(parents=True, exist_ok=True) # 폴더 없으면 생성
output_file = output_dir / 'analysis_result.png'

print(f"Saving plot to '{output_file}'...")

# 3. [핵심] 이미지 저장
fig.savefig(output_file, dpi=150, bbox_inches='tight')

# 4. [필수] 메모리 정리 (반복 저장 시 필수)
# show()를 안 쓰면 그래프가 메모리에 계속 남으므로 반드시 닫어워쟈 합니다.
plt.close(fig)

# 파일 생성 확인
if output_file.exists():
    print("검증 완료 : 이미지 파일이 생성되었습니다.")
    
