import numpy as np
import thinkdsp
# 기반 클래스/유틸/상수 끌어오기
from thinkdsp import Sinusoid, normalize, unbias, PI2


class TriangleSignal(Sinusoid):
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / PI2   # 현재까지 진행된 사이클 수 (정수+분수)
        frac, _ = np.modf(cycles) # 분수 부분만 취해 0~1 구간으로 정규화
        ys = np.abs(frac - 0.5)     # 삼각파: 0~1에서 중앙 0.5에 대해 대칭인 V자 파형
        ys = normalize(unbias(ys), self.amp)   # 평균 0로 만들고 진폭 self.amp로 정규화
        return ys

# 테스트: 200 Hz 삼각파 생성/플롯/저장
sig = TriangleSignal(freq=200, amp = 1, offset = 0.1)
wave = sig.make_wave(duration=1, framerate=44100)
wave.plot()

# 저장/재생
wave.write("triangle.wav")
wave = sig.make_wave(duration=1, framerate=44100)
wave.plot()