import numpy as np

import thinkdsp
from matplotlib import pyplot as plt

sig = thinkdsp.CosSignal(440) + thinkdsp.SinSignal(880,0.5)
wave = sig.make_wave(duration=1.0, framerate=44100)

spectrum = wave.make_spectrum()
spectrum.low_pass(cutoff=600, factor=0.01)

filterd = spectrum.make_wave()
filterd.write('temp.wav')


spectrum.plot(); plt.show()
