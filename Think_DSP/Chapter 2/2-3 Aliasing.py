import thinkdsp
import matplotlib.pyplot as plt

framerate = 10000

# duration을 늘려 파형 전체를 매끄럽게 확인
signal = thinkdsp.CosSignal(4500)
duration = 0.01  # 10ms, 여러 주기를 포함
segment = signal.make_wave(duration, framerate=framerate)
segment.plot()
plt.show()

signal = thinkdsp.CosSignal(5500)
segment = signal.make_wave(duration, framerate=framerate)
segment.plot()
plt.show()
