import thinkdsp
import matplotlib.pyplot as plt

violin_path = "/Users/kimjisoo0319/Desktop/KAIST/자료/2_신호처리/1.DSP/Study Material/violin.wav"
violin_wave = thinkdsp.read_wave(violin_path)
violin_wave.write(filename='violin.wav')
thinkdsp.play_wave(filename='violin.wav', player='afplay')
violin_wave.plot(); plt.show()
