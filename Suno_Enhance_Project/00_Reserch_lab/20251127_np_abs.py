import numpy as np
import librosa
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. STFT 수행
y, sr, duration = load_audio("test_input.wav")
D = librosa.stft(y,n_fft = 2048,hop_length = 512)

print(f"D (STFT결과) Shape: {D.shape}") # 1025, Frames
print(f"D dtype: {D.dtype}")           # complex64 복소수

# 2. np.abs로 크기(Magnitude) 추출
S = np.abs(D) # S = Magnitude (진폭)

print(f"\n--- np.abs(D) 변환 결과 ---")
print(f"S (Magnitude) Shape: {S.shape}")
print(f"S dtype: {S.dtype}")
print(f"S 깂 범위 : {S.min():.4f} ~ {S.max():.4f}")

# 무음 구간 확인 : 값이 0에 가까워야 함
# np.iscomplexobj(S)가 False인지 확인
if not np.iscomplexobj(S):
    print("✅ 검증 완료: 복소수 성분이 제거되고 실수만 남았습니다.")