from pathlib import Path

# 1) pathlib 가져오기 및 기본 사용
# 예시 1: 현재 작업 디렉터리의 Path 객체 생성
current_dir = Path.cwd() # cwd = Current Working Directory
print(f"현재 폴더: {current_dir}")

# 예시 2 : 특정 파일 경로로 Path 객체 생성
file_path = Path("C:Users/MyUser/Documents/report.docx")
print(f"파일 경로: {file_path}")

# 예시 3 : 상대 경로 사용
relative_path = Path("my_project/data/data.csv")
print(f"상대 경로: {relative_path}")
# -----------------------------------------------------------------------------------
# 2) 경로 결합 (가장 중요하고 편리한 기능)
# os.path.join()을 복잡하게 쓰지 않고, 슬래시(`/`) 연산자를 사용해 경로를 직관적으로 결합할 수 있습니다.

# 예시 1 : 기준이 되는 폴더 경로 객체를 만든다.
base_dir = Path("C:/my_app/assets")

# 예시 2 : '/' 연산자를 사용해 하위 폴더나 파일을 바로 연결한다.
image_folder = base_dir / "images"
font_file = base_dir / "fonts" / "my_font.ttf"

print(f"이미지 폴더 : {image_folder}")
print(f"폰트 파일: {font_file}")
# -----------------------------------------------------------------------------------
# 3) 파일/폴더 정보 쉽게 확인하기 ( if 문과 단짝)
# path 객체는  파일 경로를 쉽게 분해하고, 상태를 확인할 수 있는 다양한 '속성'과 '메서드'를 제공합니다.

# 분석할 예제 파일 경로
p = Path("C:/my_project/src/main.py")

print(f"경로: {p}")
print("-" * 20)
print(f"파일 이름 (확장자 포함): {p.name}")
print(f"file name (확장자 제외) : {p.stem}")
print(f"확장자: {p.suffix}")
print(f"부모 폴더: {p.parent}")
print(f"파일이 실제로 존재하는가?: {p.exists()}")
print(f"이것은 파일인가?: {p.is_file()}")
print(f"이것은 폴더인가?: {p.is_dir()}")
# ----------------------------------------------------------------------------------
# 4) 예재: if 문으로 파일 확장자 검사하기
# .wav 확장자 검사하는 예재.

# 검사할 파일 리스트 (문자열)
file_list = ["song_01.wav", "song_02.wav", "song_03.Mp3"]

print("---WAV 파일 검사 시작 ---")

for filename in file_list:
    # 1. 문자열을 path 객체로 변환
    file_path = Path(filename)
    # 2 Path 객체의 .suffix 속성 사용(확장자)하여 if문으로 검사
    if file_path.suffix == ".wav":
        print(f"[성공] '{file_path.name}'은 WAV파일 입니다.")
    else:
        print(f"[실패] '{file_path.name}'은 WAV파일이 아닙니다. (확장자: {file_path.suffix})")

    print("---검사 완료---")
# ----------------------------------------------------------------------------------
# 5) 폴더 생성 및 파일 읽기/쓰기
    # 1. 폴더 생성
    # .mkdir(parents=True, exist_ok=True)
    # parents=True: 중간 폴더가 없으면 자동으로 만들어줌 (예: 'a/b/c'에서 'a'와 'b'가 없어도 'c' 생성 가능)
    # exist_ok=True: 폴더가 이미 있어도 에러를 발생시키지 않음 (권장)
new_dir = Path("my_temp_folder/data")
new_dir.mkdir(parents=True, exist_ok=True)
print(f"'{new_dir}' 폴더 생성 완료.")

# 2. 파일 쓰기
# .write_text() : 간단한 텍스트를 파일에 씁니다. (인코딩 기본값: utf-8)
file_to_write = new_dir / "hello.txt"
file_to_write.write_text("안영하세요. Pathlib입니다.")
print(f"'{file_to_write}' 파일 쓰기 완료.")

# 3. 파일 읽기
# .read_text() : 파일의 텍스트를 읽어옵니다.
if file_to_write.exists():
    content = file_to_write.read_text()
    print(f"'{file_to_write}' 파일 읽기 내용:{content}")