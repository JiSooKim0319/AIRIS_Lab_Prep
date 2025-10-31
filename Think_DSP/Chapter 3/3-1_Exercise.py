import numpy as np
import matplotlib.pyplot as plt
import thinkdsp
from thinkdsp import Wave, play_wave


class Chirp:
    def __init__(self, f0, f1, duration=1.0, amp=1.0):
        self.f0 = f0  # 시작 주파수
        self.f1 = f1  # 끝 주파수
        self.duration = duration
        self.amp = amp

    def evaluate(self, ts):
        k = (self.f1 - self.f0) / self.duration  # 주파수 증가율
        phase = 2 * np.pi * (self.f0 * ts + 0.5 * k * ts ** 2)  # 위상 계산 (시간의 2차 함수)
        return self.amp * np.cos(phase)

    def make_wave(self, framerate=44100):
        ts = np.linspace(0, self.duration, int(framerate * self.duration))
        ys = self.evaluate(ts)
        return Wave(ys, ts, framerate)

# 사용 예시
# 2) 선형 처프 생성 (thinkdsp.ChirpSignal 이용)
chirp = Chirp(f0=500, f1=1500, duration=1.0)
# 3) 파형 생성(wave 객체)
wave = chirp.make_wave()

# 4) 파형 시각화 (시간-진폭)
wave.plot()
plt.title("Linear Chirp Signal (500 Hz to 1500 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 5) Save to Files (tone.wav)
filename = "linear_chirp.wav"
wave.write(filename)
print(f"파일 저장 완료 : {filename}")

# 6) (macOS) 시스템 기본 재생기 이용해 바로 재생
thinkdsp.play_wave(filename, player="afplay")