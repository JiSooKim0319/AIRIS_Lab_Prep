import numpy as np

import thinkdsp
from matplotlib import pyplot as plt

def __init__(self, freq=440, amp=1.0, offset=0, func=np.sin):
    Signal.__init__(self)
    self.freq = freq
    self.amp = amp
    self.offset = offset
    self.func = func

# Signal provids make_wavem, which looks like this:
def make_wave(self, duration=1, start=0, framerate=11025) :
    n = round(duration * framerate)
    ts = start + np.arange(n) / framerate
    ys = self.evlauate(ts)
    return Wave(ys, ts, framerate=framerate)

# To compute the ys, make_wave invokes ecaluate, which is provided by Sinusoid:
def evaluate(self, ts) :
    phase = PI2 * self.freq * ts + self.offset
    ys = self.amp * self.func(phase)
    return ys
