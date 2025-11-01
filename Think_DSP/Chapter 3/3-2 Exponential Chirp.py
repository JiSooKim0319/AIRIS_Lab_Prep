import numpy as np
import matplotlib.pyplot as plt
import thinkdsp


def evaluate(self, ts):
    start, end = np.log10(self.start), np.log10(self.end)
    freqs = np.logspace(start, end, len(ts)-1)
    return self._evaluate(freqs, ts)

signal = thinkdsp.ExpoChirp(start=220, end=880)
wave = signal.make_wave(duration=1)

wave.plot()
plt.show()