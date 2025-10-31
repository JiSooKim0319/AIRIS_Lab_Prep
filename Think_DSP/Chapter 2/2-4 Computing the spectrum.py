import numpy as np
from numpy.fft import rfft, rfftfreq


class wave:
    def make_spectrum(self):
        n = len(self.ys)
        d = 1 / self.framerate
        hs = rfft(self.ys)
        fs = rfftfreq(n,d)
        return Spectrum(hs, fs, self.framerate)




