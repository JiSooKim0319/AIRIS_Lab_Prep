# #1) librosa.resample()
# # 오디오의 샘플레이트를 원하는 값으로 변경하는 함수.
# # 이 작업은 데이터의 길이와 용량을 직접적으로 변화시키며, sr 옵션을 사용하지 않은 librosa.load()의 기본 기능이기도 함.
# # y = 리샘플링할 원본 오디오 데이터 배열 (`numpy` 배열)
# # orig_sr` = 원본 데이터의 샘플레이트
# # target_sr = 변경할 목표 샘플레이트
#
import librosa
from pathlib import Path
import numpy as np
import soundfile as sf
# # 에시 : 44100 Hz로 로드된 데이터를 16000Hz로 변경
#
# # 1. 원본 로드 (원본 SR 유지, sr=None 사용)
# p = Path("input_low_volume.wav")
#
# y_orig, sr_orig = librosa.load(p, sr=None)
#
# # 2. 리샘플링 수행
# TARGET_SR = 16000
# y_resampled = librosa.resample(
#     y=y_orig,
#     orig_sr=sr_orig,
#     target_sr=TARGET_SR,
# )
#
# print(f"원본 SR : {sr_orig}Hz, 길이: {len(y_orig)}")
# print(f"변경 SR : {TARGET_SR}Hz, 길이 : {len(y_resampled)}")
#
# # 2) librosa.to_mono (스테레오 -> 모노 변환)
# # 두 개 이상의 채널을 가진 스테레오 오디오 데이터를 하나의 채널(모노)로 합쳐주는 함수입니다.
# # `librosa.load()`는 기본적으로 이 작업을 자동으로 수행하지만,
# # `sr=None`이나 `mono=False` 옵션을 사용했을 경우 수동으로 변환해야 합니다.
#
# # 가상의 스테레오 데이터 생성
# # 형태 : (2, 10) 또는 (10, 2)
# y_stereo_example = np.array([
#     [0.5, 0.4, 0.3], # 왼쪽 채널
#     [0.7, 0.6, 0.5]  # 오른쪽 채널
# ])

# # to_mono 실행
# y_mono = librosa.to_mono(y_stereo_example)
#
# print(f"스테레오 형태 : {y_stereo_example.shape}")
# print(f"모노 변환 상태 : {y_mono.shape}")

# 3) 예제: `if`문과 `try`를 활용한 통합 처리
# soundfile로 원본을 유지함 로드한 후, if 문으로 채널과 샘플레이트를 검사혀 필요할 때만 변한하는 실용적인 예제.
p = Path("data/input_low_volume.wav")
TARGET_SR = 44100

try:
    y_sf, sr_orig = sf.read(p)
    print(f" 원본 : {sr_orig} Hz, 채널 {y_sf.ndim} dimensions") # ndim = 배열의 차원 수
    y_processed = y_sf
    # 2. if문으로 채널 검사 및 to_mono 적용
    if y_sf.ndim > 1:
        y_processed = librosa.to_mono(y_sf.T)
        print("-> [채널] 스테레오를 모노로 변환했습니다.")
    # 3. if문으로 샘플레이트 검사 및 resample 적용
    if sr_orig != TARGET_SR:
        y_processed = librosa.resample(
            y = y_processed,
            orig_sr = sr_orig,
            target_sr = TARGET_SR
        )
        print(f"-> [SR] {sr_orig}Hz를 {TARGET_SR}로 리샘플링링했습니다.")
    print("최종 데이터 규격 통일 완료")
except Exception as e:
    print(f"오류 발생: {e}")





