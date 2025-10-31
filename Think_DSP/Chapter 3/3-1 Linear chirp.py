import thinkdsp
import matplotlib.pyplot as plt
import numpy as np
from thinkdsp import PI2, Signal

signal = thinkdsp.Chirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=44100)

class Chirp(Signal):
    def __init__(self, start=440, end=880, amp=1.0):
        self.start = start
        self.end = end
        self.amp = amp

def evaluate(self, ts):
    freqs = np.linspace(self.start, self.end, len(ts))
    dts = np.diff(ts, prepend=0.0)
    dphis = PI2 * freqs * dts
    phases = np.cumsum(dphis) # np.insert(phases, 0, 0)
    ys = self.amp * np.cos(phases)
    return ys



wave.write('chirp.wav')
wave.plot()
plt.show()
