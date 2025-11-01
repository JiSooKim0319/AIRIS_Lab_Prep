# filename: spectrogram_thinkdsp_demo.py

import numpy as np
import matplotlib.pyplot as plt
import thinkdsp

# 1) 선형 처프 신호(220→440 Hz, 1초, 11025 Hz) 생성
signal = thinkdsp.Chirp(start=220, end=440)           # thinkdsp에 Chirp가 있을 때
wave = signal.make_wave(duration=1.0, framerate=11025)

# 2) 스펙트로그램 생성(seg_length=512 → 창 길이)
spectrogram = wave.make_spectrogram(seg_length=512)

# 3) 위: 스펙트로그램(700 Hz까지만 표시), 아래: 파형
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
spectrogram.plot(high=700)                             # 상단: 시간-주파수(세기)
plt.title("Spectrogram (0–700 Hz)")

plt.subplot(2,1,2)
wave.plot()                                           # 하단: 시간-진폭
plt.title("Waveform")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
