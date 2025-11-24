# 1) sf.write() 기본 문법
# sf.write(file, data, samplerate, subtype) 형태로 사용하며, Numpy 배열을 파일 포맷으로 변환하는 역할 수행

# 2) Test Code
import numpy as np
import soundfile as sf
from pathlib import Path

# 1. 파라미터 정의
OUTPUT_FILENAME = "test_output.wav"
SR = 44100
DURATION_SEC = 2
N_SAMPLES = int(SR * DURATION_SEC)

# 2. 임이의 Numpy 배열 (랜덤 소음) 생성 및 안전장치 적용
# 노이즈 생성 ( 일부러 1을 넘을 가능성이 있는 높은 진폭으로 설정)
raw_noise = np.random.randn(N_SAMPLES).astype(np.float32) * 1.5

# np.clip 적용
y_safe_data = np.clip(raw_noise, -1.0, 1.0)

# 3. 파일 저장 실행 (sf.write)
print(f" {DURATION_SEC}초 노이즈 파일 저장 시도 중...")

try:
    # 1. 안전한 데이터 soundfile.write로 저장함
    sf.write(OUTPUT_FILENAME, y_safe_data, SR) # subtype 자동으로 PCM_16으로 저장됨
    # 2. (TEST) Path 객체를 사용하여 파일 존재 여부 최종 확인
    output_path = Path(OUTPUT_FILENAME)
    if output_path.exists():
        print(f"성공 : 파일 '{OUTPUT_FILENAME}'이 생성 되었습니다.")

except Exception as e:
    print(f"오류 : soundfile.write 실행 중 오류 발생: {e}")
