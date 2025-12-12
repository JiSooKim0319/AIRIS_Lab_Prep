# # 2) `librosa.load()`의 기본 문법 (자동 변환)
# # librosa.load() 역시 두 개의 값을 반환합니다: (1) 오디오 데이터, (2) 샘플레이트.
#
# import librosa
# from pathlib import Path
#
# # 읽어올 파일 경로 (MP3, WAV 등 지원)
# file_path = Path("my_song.mp3")
#
# try:
#     # y: 데이터, sr: samplerate
#     y, sr = librosa.load(file_path)
#
#     print(f"파일 : {file_path}")
#     print(f"샘플레이트 : {sr} Hz")
#     print(f"데이터 형태 (Shape) : {y.shape}")
#     print(f"데이터 타입 (dtype) : {y.dtype}")
#
# except Exception as e:
#     print(f"파일을 읽는 중 오류가 발생하였습니다: {e}")
#
# # 4) 예제: `if`문으로 오디오 길이 및 형식 검사
# # librosa.load()`를 통해 얻은 정보를 기반으로 코드를 검증하는 예제
#
# audio_path = Path("test_audio.wav")
#
# if audio_path.exists():
#
#     # 1. 44100으로 샘플레이트 변환 (soundfile의 통일성을 위하여)
#     y, sr = librosa.load(audio_path, sr = 44100)
#
#     # 2. duration 계산
#     # len(y)는 샘플의 총 개수, 이것을 sr(초당 샘플 수)로 나누면 초(second)가 됨.
#     duration_sec = len(y) / sr
#     print(f"Samplerate: {sr} Hz, duration: {duration_sec:.2f} 초") #duration_sec:.2f -> 포맷지정자 : 소수점 2자리까지.
#
#     # 3. if 문으로 오디오 길이 검사 ( 예 : 10초를 초과하면 경고)
#     if duration_sec > 10:
#         print("오디오 길이가 10초를 초과하여 처리 시간이 길어질 수 있습니다.")
#     else:
#         print("오디오 길이가 적절합니다.")
# else:
#     print(f"{audio_path} 파일을 찾을 수 없습니다.")

# --------------------------------------------------
import numpy as np
import soundfile as sf
import librosa
from pathlib import Path
import os


# -----------------------------------------------------------
# 1. 테스트 환경 설정 (주석을 해제하고 실행하여 임시 파일을 만드세요)
# -----------------------------------------------------------
# 이 코드는 실제로 작동하는 MP3/WAV 파일이 필요합니다.
# 테스트를 위해 'test_audio.wav' 파일을 준비하거나,
# 아래 코드를 사용하여 더미(Dummy) 파일을 생성하세요.
#
# sr_test = 22050
# # 3초 길이의 낮은 볼륨의 더미 오디오 데이터 생성 (0.1로 최대 볼륨 설정)
# dummy_y = np.random.randn(sr_test * 3) * 0.1
# sf.write('input_low_volume.wav', dummy_y, sr_test)
# print("입력 테스트 파일 'input_low_volume.wav' 생성 완료.")


# -----------------------------------------------------------
# 2. 함수 정의: normalize_and_save()
# -----------------------------------------------------------
def normalize_and_save(input_path_str: str, output_path_str: str):
    """
    오디오 파일을 44100 Hz로 로드하고 볼륨 정규화 후 WAV 파일로 저장합니다.
    """
    # 입력/출력 경로를 Path 객체로 변환
    input_path = Path(input_path_str)
    output_path = Path(output_path_str)

    STANDARD_SR = 44100  # 표준 샘플레이트 설정

    # 1. 파일 유효성 검사 (if/exists)
    if not input_path.exists() or input_path.is_dir():
        print(f"❌ 오류: 입력 파일 '{input_path.name}'을 찾을 수 없거나 폴더입니다.")
        return

    try:
        # 2. 로드 (librosa): 44100 Hz로 리샘플링하며 float 데이터로 로드
        #    librosa는 mp3, wav 등을 모두 지원합니다.
        print(f"🔄 파일 로드 및 {STANDARD_SR}Hz로 리샘플링 중...")
        y, sr = librosa.load(input_path, sr=STANDARD_SR)

        # 3. 오디오 데이터 정규화 (핵심 처리 로직)
        #    최대 진폭을 찾습니다. np.abs는 진폭의 절대값(음수->양수)을 구합니다.
        max_amp = np.max(np.abs(y))

        #    최대 진폭으로 전체 데이터를 나누어 -1.0 ~ 1.0 범위로 확장 (볼륨 키우기)
        #    max_amp가 0일 경우(무음)를 대비하여 0.0001을 더해 오류 방지
        y_normalized = y / (max_amp + 0.0001)
        print(f"   - 정규화 완료. 최대 볼륨 {max_amp:.4f} -> 1.0")

        # 4. 파일 저장 (soundfile): 처리된 데이터를 WAV 파일로 저장
        #    soundfile.write는 NumPy 배열을 직접 파일로 저장합니다.
        sf.write(output_path, y_normalized, STANDARD_SR)

        print(f"✅ 성공: '{output_path.name}' 파일이 저장되었습니다.")

    except Exception as e:
        print(f"🛑 처리 중 예외 발생: {e}")


# -----------------------------------------------------------
# 3. 함수 호출 및 테스트
# -----------------------------------------------------------
# 주의: 'input_low_volume.wav' 파일이 현재 실행 폴더에 있어야 합니다.
normalize_and_save(
    input_path_str='data/input_low_volume.wav',
    output_path_str='data/output_normalized.wav'
)

# 테스트용 임시 파일 정리 (선택 사항)
# os.remove('input_low_volume.wav')
