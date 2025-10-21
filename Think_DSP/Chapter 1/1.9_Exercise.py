import thinkdsp
import numpy as np
import matplotlib.pyplot as plt

# 1.1-2
# violin_path = 'violin.wav'
# violin_wave = thinkdsp.read_wave(violin_path)
# violin_wave.write('violin.wav'); plt.show()
#
# spectrum = violin_wave.make_spectrum()
# spectrum.low_pass(cutoff=600, factor = 0.01)
# spectrum.high_pass(cutoff=400, factor = 0.01)
# spectrum.plot(); plt.show()


# 1.3

# 1) 신호 합성 (Signal 단계)
# cos_sig = thinkdsp.CosSignal(freq = 440, amp = 1, offset = 0)
# sin_sig = thinkdsp.SinSignal(freq = 880, amp = 4, offset = 0)
# mix = cos_sig + sin_sig
#
# # 2) 샘플링하여 Wave 만들기
# sig_wave = mix.make_wave(duration = 3, start=0, framerate=11025 )
#
# # 3) 파일로 저장( 이제 wave 메서드 사용 가능)
# sig_wave.write("Mix.wav")
#
# # 4) 파형 보기
# sig_wave.plot() ; plt.show()
#
# # 5) 스펙트럼 만들기 → 필터 적용
# spectrum = sig_wave.make_spectrum()
# spectrum.low_pass(cutoff=600, factor=0.01)
# after_lp = spectrum.make_wave()
#
# # 6) 스펙트럼 보기
# spectrum.plot(); plt.show()
#
#
# plt.show()


# Exe) 1-4 : Wave의 재생 속도를 s배로 조절하는 함수
# s > 1 : 더 빠르게 (길이 짧아짐, 피치 올라감)
# s < 1 : 더 느리게 (길이 길어짐, 피치 내려감)

import thinkdsp
from matplotlib import pyplot as plt

def stretch(wave, s: float):
    if s <= 0:
        raise ValueError("strectch factor s must be positive")

    wave.ts /= s  # 1) 시간축을 s배 '압축/팽창' (빠르게: 1/s로 줄이기)
    wave.framerate *= s  # 2) 재생 샘플레이트를 s배로 조정 (빠르게 : 더 큰 framerate)


# 1) 440Hz 코사인 1초 생성
sig = thinkdsp.CosSignal(440, 1)
wave = sig.make_wave(duration=1, framerate=44100)

print("Before:", wave.duration, wave.framerate)

# 2) 2배 빠르게(길이 절반, 피치 2배로)
stretch(wave, 2.0)
print("After:", wave.duration, wave.framerate)

# 3) 시각 확인 : 같은 초기 구간을 비교하기 위해 segment 사용(선택)
seg = wave.segment(start=0.0, duration=0.5)
plt.plot() ; plt.title("Stertched (2x faster)") ; plt.show()

# 4) 파일로 저장하기
wave.write("tone_fast.wav")
thinkdsp.play_wave("tone_fast.wav", player="afplay" )



