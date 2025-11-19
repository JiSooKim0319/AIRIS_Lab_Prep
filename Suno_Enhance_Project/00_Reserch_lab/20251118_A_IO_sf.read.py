import soundfile as sf
from pathlib import Path

# 2) sf.read()`의 기본 문법 (가장 중요)**
# 읽어올 파일 경로
file_path = Path("my_audio.wav") # pathlib과 호환가능.

try:
    # 1. 파일 읽기 시도
    # data 변수에는 오디오 파형이, samplerate 변수에는 샘플레이트가 저장됩니다.
    data, samplerate = sf.read(file_path)

    # 2. 정보 출력
    print(f"File: {file_path}")
    print(f"Samplerate: {samplerate} Hz")
    print(f"Shape: {data.shape}")
    print(f"dtype: {data.dtype}")

except Exception as e:
    print(f"Error: {e}")
 #--------------------------------------------------------------------------------
# 3) `if`문과 함께 사용하기 (파일 검사)
# sf.read()는 pathlib의 .exists() 및 if 문과 함께 사용하여 코드를 안전하게 만듬.

# 사용자의 목표였던 ".wav"파일만 골라서 읽는 예제.
p = Path("song_01.wav")

    # 1. 존재하는지, 그리고 파일인지 확인
if p.exists() and p.is_file():
    # 2. 확장자(suffix)가 .wav인지 확인
    if p.suffix == "wav.":
        print(f"'{p.name}'은 WAV파일입니다. 읽기를 시도합니다.")
        try:
            data, samplerate = sf.read(p)
            print(f"읽기 성공! 샘플레이트 : {samplerate} Hz")

            # 3. 샘플레이트 값으로 추가 검사
            if samplerate != 44100:
                print(f"[경고] 이 파일은 표준 CD음질 (44100Hz)가 아닙니다.")
        except Exception as e:
            print(f"{p.name}' 파일 읽기 실패:{e}")
    elif p.suffix == "mp3":
        print(f"'{p.name}'은 MP3 파일입니다. 읽기를 시도합니다.")
        try:
            data, samplerate = sf.read(p)
            print(f"읽기 성공! 샘플레이트 : {samplerate} Hz")

            # 3. 샘플레이트 값으로 추가 검사
            if samplerate != 44100:
                print(f"[경고] 이 파일은 표준 CD음질 (44100Hz)가 아닙니다.")
        except Exception as e:
            print(f"{p.name}' 파일 읽기 실패:{e}")
    else:
        print(f"'{p.name}'는 WAV or MP3 파일이 아닙니다. (확장자: {p.suffix})")
else:
    print(f"'{p.name}' 파일을 찾을 수 없습니다.")


