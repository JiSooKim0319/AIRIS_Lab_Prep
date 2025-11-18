from pathlib import Path

# 1) exists()의 기본 문법 및 역할
# path 객체의 .exists() 메서드를 호출하면, 해당 경로가 파일 시스템에 존재하면 True를, 존재하지 않으면 False 를 반환합니다.

# 예시 1: 실제로 존재할 가능성이 높은 경로)
# 윈도우 사용자 예시
p_window = Path("C:/Windows")
print(f"'{p_window}' 는 존재하는가? : {p_window.exists()}")

# 예시 2 : 존재하지 않을 가능성이 높은 경로
p_fake = Path("C:/MyFakeFolder/non_existent_file.txt")
print(f"'{p_fake} 는 존재하는가? : {p_fake.exists()}")

# 예시 3 : 현재 작업 폴더
p_current = Path.cwd()
print(f"'{p_current}' 는 존재하는가?: {p_current.exists()}")
# ----------------------------------------------------------------------------------------
# 2) .exists()와 if문의 결합 (가장 중요한 활용법)
# 파일을 읽거나 쓰기 전에 `.exists()`로 먼저 확인하면,
# `FileNotFoundError`와 같은 예외(오류)를 사전에 방지할 수 있습니다.
# (LBYL: Look Before You Leap)*

# 1. 파일 읽기 전 확인
config_file = Path("settings.ini")

if config_file.exists():
    print(f"'{config_file}' 파일을 발견했습니다. 설정을 읽어옵니다.")
        # 실제 읽기 로직
        # content = config_file.read_text()
else:
    print(f"'{config_file}' 파일을 찾을 수 없습니다. 기본 설정을 사용합니다.")

# 2. 폴더 생성 전 확인 (.mkdir()과 연계)
data_folder = Path("data")

if data_folder.exists():
    print(f"'{data_folder}' 폴더는 이미지 존재합니다.")
else:
    print(f"'{data_folder}' 폴더가 존재 하지 않아 새로 생성합니다.")
    data_folder.mkdir(parents=True, exist_ok=True)
    print(f"'{data_folder}' 폴더 생성 완료.")
    file_to_write = data_folder / "hello.txt"
    file_to_write.write_text("안녕하세요. Pathlib입니다.")
    print(f"'{file_to_write}' 파일 쓰기 완료.")

    if file_to_write.exists():
        content = file_to_write.read_text()
        print(f"'{file_to_write}' 파일 읽기 내용:{content}")
# ----------------------------------------------------------------------------------------
