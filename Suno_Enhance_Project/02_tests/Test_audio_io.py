import sys
import numpy as np
import librosa
import soundfile as sf
from pathlib import Path


# --- [1] Load Audio 함수 ---
def load_audio(input_path: str, target_sr: int = 44100, mono: bool = True):
    p = Path(input_path)

    # 1. 파일 존재 여부 확인
    if not p.exists():
        print(f"❌ Error: File '{input_path}' does not exist")
        sys.exit(1)

    # 2. 확장자 확인
    if not (p.suffix.lower() == ".wav" or p.suffix.lower() == ".mp3"):
        print(f"❌ Error: File '{p.suffix}' is not a .wav or .mp3 file")
        sys.exit(1)

    try:
        print(f"📂 Loading audio from '{p.name}'...")
        # 3. 데이터 로드 (librosa)
        y, sr = librosa.load(p, sr=target_sr, mono=mono)

        # 4. 길이 검사 (가드 클로즈)
        duration = librosa.get_duration(y=y, sr=sr)
        if duration > 300:
            raise Exception(f"Audio duration is too long ({duration:.2f}s)")

        return y, sr, duration

    except Exception as e:
        print(f"❌ Failed to load audio: {e}")
        sys.exit(1)


# --- [2] Save Audio 함수 ---
def save_audio(output_path: str, data: np.ndarray, sr: int = 44100, subtype: str = 'PCM_16'):
    """
    오디오 데이터를 지정된 포맷으로 안전하게 파일에 저장합니다.
    Args:
        output_path (str): 저장할 파일의 경로
        data (np.ndarray): 저장할 오디오 데이터 (float32)
        sr (int): 샘플레이트
        subtype (str): 저장 포맷 ('PCM_16' 등)
    """
    p = Path(output_path)

    # 1. 데이터 유효성 검사
    if data is None or data.size == 0:
        print("❌ Error: 저장할 오디오 데이터가 없습니다 (Empty Data).")
        sys.exit(1)

    # 2. 데이터 클리핑 방지 (안전장치)
    data_safe = np.clip(data, -1.0, 1.0)

    try:
        # 3. 폴더 자동 생성
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            print(f"📂 폴더가 생성되었습니다: '{p.parent}'")

        # 4. 파일 쓰기
        print(f"💾 Saving audio to '{p.name}'...")
        sf.write(file=str(p), data=data_safe, samplerate=sr, subtype=subtype)

        # 5. 저장 확인
        if p.exists():
            print(f"✅ 성공: 파일이 정상적으로 저장되었습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: 파일 저장에 실패했습니다.\n   오류 내용: {e}")
        sys.exit(1)


# --- [3] 실행 테스트 (Main) ---
if __name__ == "__main__":
    print("--- 🚀 Audio Engine I/O Test Start ---")

    # 1. 테스트용 파일 경로 (본인의 파일이 있다면 경로를 수정하세요!)
    # 파일이 없으면 자동으로 테스트용 노이즈를 생성해서 저장부터 테스트합니다.
    input_file = "my_test_song.mp3"
    output_file = "processed_output/result.wav"

    # [시나리오]
    # 파일이 있으면: Load -> Save
    # 파일이 없으면: Create Noise -> Save -> Load Check

    if Path(input_file).exists():
        # A. 실제 파일 테스트
        y, sr, dur = load_audio(input_file)
        print(f"   -> Loaded: {len(y)} samples, {dur:.2f} sec")
        save_audio(output_file, y, sr)
    else:
        # B. 더미 데이터 테스트 (파일이 없을 때)
        print(f"ℹ️ '{input_file}' 파일이 없어 테스트용 노이즈를 생성합니다.")
        dummy_sr = 44100
        # 3초짜리 랜덤 노이즈 생성
        dummy_data = np.random.randn(dummy_sr * 3).astype(np.float32) * 0.5

        # 저장 테스트
        save_audio(output_file, dummy_data, dummy_sr)

        # 저장된 거 다시 불러와서 확인
        print("\n🔄 저장된 파일 다시 읽기 검증:")
        y_reloaded, sr_reloaded, dur_reloaded = load_audio(output_file)
        print(f"   -> 검증 완료: {dur_reloaded:.2f}초 데이터 확인됨.")

    print("\n--- ✨ Test Complete ✨ ---")