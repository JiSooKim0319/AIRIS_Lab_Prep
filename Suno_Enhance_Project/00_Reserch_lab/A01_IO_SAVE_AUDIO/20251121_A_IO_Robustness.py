import numpy as np
import soundfile as sf
from pathlib import Path
import os
import shutil

# 1. 파라미터 정의
# 없는 폴더 의도적으로 지정하여 테스트.
OUTPUT_DIR = "temp_output_folder"
OUTPUT_FILENAME = Path(OUTPUT_DIR) / "test_final.wav"
SR = 44100
N_SAMPLES = int(SR * 2)

# 2. 데이터 준비 및 클리핑
raw_noise = np.random.randn(N_SAMPLES).astype(np.float32) * 1.5
y_safe_data = np.clip(raw_noise, -1.0, 1.0)

# 3. 파일 저장 및 실행
print(f" 파일 저장 시도 : 경로 '{OUTPUT_FILENAME}'")
try:
    # 1. [폴더 자동 생성] 부모 폴더가 없으면 만들어 줌.
    # mkdir()을 호출하기 전에 Path 객체에서 .parent를 먼저 호출하여 폴더 경로만 추출.
    OUTPUT_FILENAME.parent.mkdir(parents=True, exist_ok=True)

    # 2. sf.write 실행(저장)
    sf.write(str(OUTPUT_FILENAME), y_safe_data, SR) # sf.write는 str 타입을 선호함.

    # (Test) 파일 존재 여부 최종 확인
    if OUTPUT_FILENAME.exists():
        print(f" 성공 : 폴더가 자동 생성됨, 파일 정상 저장.")
except Exception as e:
    # 쓰기 권한 에러, 디스크 공간 부족 등 예상치 못한 오류들 여기서 잡기.
    print(f"오류 발생 : 파일 저장에 실패함.\n 오류 내용 : {e}")
finally:
    if Path(OUTPUT_DIR).exists():
        shutil.rmtree(OUTPUT_DIR)
        print(f"테스트 폴더 '{OUTPUT_DIR}' 삭제 완료.")

