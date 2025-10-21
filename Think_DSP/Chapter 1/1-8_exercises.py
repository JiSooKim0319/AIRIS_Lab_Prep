import thinkdsp
import matplotlib.pyplot as plt

# Exercise 1.1

violin_path = "/Users/kimjisoo0319/Desktop/KAIST/자료/2_신호처리/1.DSP/Study Material/violin.wav"
violin_wave = thinkdsp.read_wave(violin_path)
violin_wave.write(filename="violin.wav")
spectrum = violin_wave.make_spectrum()
spectrum.low_pass(cutoff=600, factor=0.01)
spectrum.plot()
thinkdsp.play_wave(filename="violin.wav", player="afplay")
violin_wave.plot() ; plt.show()



