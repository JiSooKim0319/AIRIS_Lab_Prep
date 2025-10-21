import thinkdsp
import matplotlib.pyplot as plt

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)
mix = cos_sig + sin_sig

wave = mix.make_wave(duration=0.1, start=0, framerate=11025 )
wave.plot()
plt.show()

period = mix.period
segment = wave.segment(start=0, duration=period*3)

