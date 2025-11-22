# 1) `np.clip()`의 기본 문법**

# `np.clip(배열, 최솟값, 최댓값)` 형태로 사용합니다.
# - 범위 내의 값: 그대로 유지됩니다. (예: `0.5` -> `0.5`)
# - 최솟값보다 작은 값:최솟값으로 바뀝니다. (예: `-5.0` -> `-1.0`)
# - 최댓값보다 큰 값: 최댓값으로 바뀝니다. (예: `2.0` -> `1.0`)

import numpy as np
import soundfile as sf
# test: 범위를 벗어나는 값들이 포함된 배열
raw_date = np.array([2.0, -5.0, 0.5, -0.8, 1.5])
print(f"원본 데이터: {raw_date}")

# 적용: -1.0 ~ 1.0 사이로 값 제한하기
clipped_data = np.clip(raw_date, -1.0, 1)

print(f"클리핑 적용 후 : {clipped_data}")

# 2) 오디오 저장 시 np.clip이 필요한 이유 (save_audio)
# librosa로 작업할 때는 float32 실수형을 쓰지만, wav 파일로 저장할 때는 보통 int16 정수형으로 변환되어 저장됨.
# 이 변환 과정에서 `1.0`을 넘는 값은 오버플로우(Overflow)를 일으키거나 노이즈가 될 수 있습니다.
# 따라서 저장 직전에 **안전장치**로 반드시 `clip`을 걸어줘야 함.

def save_audio(path, data, sr):
    data_safe = np.clip(data, -1.0, 1)
    sf.write(path, data_safe, sr)

