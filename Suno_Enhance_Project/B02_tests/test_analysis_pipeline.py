import sys
import os
from pathlib import Path

# [경로 설정] 프로젝트 루트를 path에 추가하여 모듈 import가 가능하게 함
# 현재 파일 위치(00_Research_lab)에서 두 단계 상위 폴더를 루트로 인식
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# --- 만든 모듈들 가져오기 ---
try:
    from A01_src.A_core_audio_engine.A01_IO_DATA.audio_io import load_audio
    from A01_src.A_core_audio_engine.A02_signal_processing.Spectrogram import compute_spectrogram, save_analysis_plot
    from A01_src.A_core_audio_engine.A02_signal_processing.features import extract_features

    print("✅ 모든 모듈 Import 성공!")
except ImportError as e:
    print(f"❌ 모듈 Import 실패: {e}")
    print("폴더 구조와 __init__.py 파일을 확인해주세요.")
    sys.exit(1)

# --- 통합 테스트 실행 ---
if __name__ == "__main__":

    # 설정
    TEST_INPUT = "test_input.wav"  # 테스트할 오디오 파일
    OUTPUT_DIR = "outputs"  # 결과 저장할 폴더
    OUTPUT_FILENAME = "integration_test_result.png"

    output_path = Path(OUTPUT_DIR) / OUTPUT_FILENAME

    print(f"\n🚀 [Integration Test] Start processing '{TEST_INPUT}'...")

    # ---------------------------------------------------------
    # (Step 1) Load Audio (Module 01)
    # ---------------------------------------------------------
    print("Step 1: Loading Audio...")
    try:
        y, sr, duration = load_audio(TEST_INPUT)
        print(f"   -> Loaded successfully: {duration:.2f}s, SR={sr}")
    except Exception as e:
        print(f"❌ Step 1 Failed: {e}")
        sys.exit(1)

    # ---------------------------------------------------------
    # (Step 2) Compute Spectrogram & Features (Module 02)
    # ---------------------------------------------------------
    print("Step 2: Computing Spectrogram & Features...")
    try:
        # A. 스펙트로그램 계산
        S_dB, S = compute_spectrogram(y)

        # B. 특징(RMS, Centroid) 추출
        # (save_analysis_plot 함수가 이 데이터들을 필요로 하므로 같이 추출합니다)
        feats = extract_features(y, sr, S=S)

        print(f"   -> Spectrogram shape: {S_dB.shape}")
        print(f"   -> Features extracted: RMS, Centroid")
    except Exception as e:
        print(f"❌ Step 2 Failed: {e}")
        sys.exit(1)

    # ---------------------------------------------------------
    # (Step 3) Save Visualization Image (Module 02)
    # ---------------------------------------------------------
    print("Step 3: Saving Visualization...")
    try:
        # 결과 폴더 생성
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # 종합 리포트 저장 (우리가 만든 만능 함수 사용)
        save_analysis_plot(
            S_dB=S_dB,
            rms=feats['rms'],
            cent=feats['centroid'],
            times=feats['times'],
            sr=sr,
            output_path=str(output_path),
            title="Integration Test Result"
        )
    except Exception as e:
        print(f"❌ Step 3 Failed: {e}")
        sys.exit(1)

    # ---------------------------------------------------------
    # (Step 4) Final Check Message
    # ---------------------------------------------------------
    print("\n✅ [SUCCESS] 통합 테스트 완료!")
    print(f"👉 확인 요망: '{output_path}' 파일을 열어보세요.")
    print("   1. 위쪽: 스펙트로그램이 선명하게 보이는가?")
    print("   2. 위쪽: 하얀색 Centroid 선이 그려져 있는가?")
    print("   3. 아래쪽: 빨간색 RMS 그래프가 그려져 있는가?")