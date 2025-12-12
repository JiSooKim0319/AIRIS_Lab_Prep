# 1) librosa.stft 기본 사용법
# n_fft (Window Size): 한 번에 분석할 조각의 크기
# hop_length (Stride) : 옆으로 이동하는 간격. 보통 n_fft / 4를 사용
# window : 소리르 자를 때 양 끝을 부드롭게 다듬어주는 함수 ( "기본 값 : hann")

# import librosa
# from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio
#
# # 1. 데이터 로드 (Time Domain)
# y, sr, duration= load_audio("test_input.wav")
#
# # 2. STFT 수행 (Frequency Domain 변환)
# # 결과 D는 복소수 행렬
# D = librosa.stft(y,n_fft=2048, hop_length=512)
#
# # 3. 결과 확인
# print(f"Waveform shape: {y.shape}")     # (N,) -> 1차원 선
# print(f"Spectrogram shape: {D.shape}")  # (1 + n_fft/2, Frames) -> 2차원 지도
# print(f"Data Type: {D.dtype}")          # complex64 (복소수)

import numpy as np
import librosa
from Suno_Enhance_Project.A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio

# 데이터 로드
# 1. 파라미터 정의
N_FFT = 2048
HOP_LENGTH = 512

# 2. 데이터 로드
y, sr, duration= load_audio("../test_input.wav")
D = librosa.stft(y,n_fft=N_FFT, hop_length=HOP_LENGTH) # 질문1 : Hop_length는 왜 보통 n_fft/4를 사용하는가?


# 3. 프레임 개수 계산: 전체 길이를 간격으로 나눔
n_frames = 1 + (len(y) - N_FFT) // HOP_LENGTH # 질문2 : 이 식은 어떻게 해서 만들어진 것인가? 수학적 공식인 것인가? 나는 이 공식을 외워야 하는가? 무슨 원리인가?
stft_matrix = [] # 질문 3: stft_matrix란 무엇이고, 왜 []이렇게만 남겨 놨는가?

# 4. Loop : 프레임별로 잘라서 FFT 수행
for i in range(n_frames): # 질문 4 : 이것은 파이썬 질문임 for i range(n_frames)는 i만큼 n_frames를 계산 하라는 뜻인가? 무슨 말이야? 이해가 안됨 for range 이거에 대해서
    start = i * HOP_LENGTH # 질문 5: 시작은 왜 i * Hop_length인가? 무엇을 위해? 뭐 떄문에?
    end = start + N_FFT # 질문 6: 왜 끝지점은 시작 + N_fft인가?

    # A. 자르기
    segment = y[start:end] # 질문 7: 세그먼트 = y(start:end)라는 것은 시작과 끝의 중간지점이라는 거야?이게 무슨 말이야 시작 : 끝 이 수식의 의미를 모르겠음.

    # B. 윈도우 함수 적용 (Windowing)
    windowed_segment = segment * np.hanning(N_FFT)

    # C. FFT 수행
    # 결과는 복소수로 나옴
    spectrum = np.fft.rfft(windowed_segment)
    stft_matrix.append(spectrum) # 질문 8 : append가 뭐였는지 기억이 안남. stft_matrix는 아까 []이렇게 나왔는데 왜 append(spectrum)을 하는가? 왜? 무엇을 얻고자?

# 3. 결과 뒤집기 : 시간 ,주파수 -> 주파수, 시간 # 질문 9: 왜 결과를 뒤집어야 하는가?
my_stft = np.array(stft_matrix).T # 질문 10 : array는 무엇이고, T는 무엇인가 왜 여기에 붙는가?

# ---검증---
librosa_stft = librosa.stft(y, n_fft=N_FFT, hop_length=HOP_LENGTH, center=False) # 질문 11 ; centrt = False를 왜 붙이는건가?

print(f"내 구현 Shape: {my_stft.shape}")
print(f"Librosa Shape: {librosa_stft.shape}") # librosa shape를 왜 보는 것이고 내 구현 shape랑 뭔 차이인가?
# 구조가 같은지 확인
print(f"구조 일치 여부: {my_stft.shape == librosa_stft.shape}")