import os
from pathlib import Path
from typing import Dict, Any, Optional
import mutagen

def extract_metadata(file_path:str) -> Dict[str, Any]:
    """
    오디오 파일의 헤더 정보를 추출 ->  Analyzer에게 전달

    Args:
        file_path (str): 오디오 파일 경로

    Returns:
        Dict: {
            "format": str,          # mp3, wav, flac 등
            "bitrate_kbps": int,    # 128, 320, 1411(wav) 등
            "sample_rate": int,     # 44100, 48000 등
            "channels": int,        # 1(Mono), 2(Stereo)
            "duration_sec": float,  # 파일 길이
            "file_size_mb": float   # 파일 크기
    """
    p = Path(file_path)

    # 기본값 설정 (실패 시 반환)
    metadata = {
        "file_path": str(p),
        "format": "unknown",
        "bitrate_kbps": 0,
        "sample_rate": 0,
        "channels": 0,
        "duration_sec": 0.0,
        "file_size_mb": 0.0,
        "error": None
    }

    if not p.exists():
        metadata["error"] = "File not found"
        return metadata

    try:
        # 1. 파일 크기 측정
        metadata["file_size_mb"] = round(p.stat().st_size / (1024 * 1024))
        metadata["format"] = p.suffix.lower().replace(".", "")

        # 2. Mutagen으로 헤더 파싱
        audio = mutagen.File(file_path)

        if audio is None:
            metadata["error"] = "Unsupported audio format or corrupt file"
            return metadata

        # 3. 정보 추출
        if hasattr(audio.info, "bitrate") and audio.info.bitrate:
            metadata["bitrate_kbps"] = int(audio.info.bitrate / 1000)

        # WAV/FLAC 등 비트레이트 정보가 없는 경우 0으로 둠 (Analyzer가 0이면 '고음질'로 간주하게 로직 위임)
        if hasattr(audio.info, "sample_rate"):
            metadata["sample_rate"] = audio.info.sample_rate

        if hasattr(audio.info, "channels"):
            metadata["channels"] = audio.info.channels

        if hasattr(audio.info, "duration_sec"):
            metadata["duration_sec"] = audio.info.duration_sec

    except Exception as e:
        metadata["error"] = str(e)

    return metadata