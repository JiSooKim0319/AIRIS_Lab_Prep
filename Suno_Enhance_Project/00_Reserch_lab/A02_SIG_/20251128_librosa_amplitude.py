import numpy as np
import librosa
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 1. 이전 단계 (Load -> STFT -> Abs)
y, sr, duration = load_audio("../test_input.wav")
D = librosa.stft(y, n_fft=2048, hop_length=512) # stft =  # D는 원본 데이터(복소수)
S = np.abs(D) # linear Amplitude # S는 복소수 -> 진폭 변환

# 2. 데시벨 변환 (Amplitude to dB)
# ref = np.max: 데이터 중 가장 큰 값을 0 dB로 기준 잡겠다는 뜻 (Relative Scale)
S_dB = librosa.amplitude_to_db(S, ref=np.max) # amplitude는 진폭 변환(선형적) 된 것 -> dB로 변환 (로그 스케일)

print(f"---변환 전후 데이터 비교---")
print(f"Linear(S) 범위 : {S.min():.4f} ~ {S.max():.4f}")

print(f"Log(S_dB) 범위 : {S_dB.min():.2f} ~ {S_dB.max():.2f} dB")
# 예상 : -80.0 dB ~ 0.00 dB (최대값이 0으로 고정됨)

# check 시각화를 위한 준비가 되었는가?
# 최대값이 0 근처여야 직관적인 시각화가 가능.
if np.isclose(S_dB.max(), 0.0):
    print( " 검증 완료 : 0 dB 기준으로 정규화 되었습니다.")

