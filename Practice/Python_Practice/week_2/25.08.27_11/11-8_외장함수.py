# Google ==> list of pythin modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# import os
#
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder,"폴더를 생성하였습니다.")
#
# print(os.listdir())

import time
print(time.strftime("%A, %B %d, %Y", time.localtime()))

import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days = 1)
print("내일은", today + td)
