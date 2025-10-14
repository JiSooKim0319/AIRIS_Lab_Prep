# score_file = open("score.txt", "w", encoding="utf-8")
# print("Max :100", file=score_file)
# print("전공실기 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("관혁악법 : 80")
# score_file.write("\n전자음악프로그래밍 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 안의 정보를 모르는 것일 때, 외부 자료
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline() # 한줄씩 처리하기에 = 메모리 효율적
#     if not line:
#         break
#     print(line, end="")
# score_file.close()



score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장, 파일 전체 한 번에 리스트로 들고 있으니, 메모리 부담 큼
for line in lines:
    print(line, end="")
score_file.close()