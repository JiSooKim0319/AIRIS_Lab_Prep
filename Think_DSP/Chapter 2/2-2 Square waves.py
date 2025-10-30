import numpy as np
import thinkdsp
# 기반 클래스/유틸/상수 끌어오기
from thinkdsp import Sinusoid, normalize, unbias, PI2



class SquareSignal(sinusoid) :
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / PI2
        frac, _ =np.modf(cycles)
        ys = self.amp * np.sign(unbias(frac))
        return ys
    