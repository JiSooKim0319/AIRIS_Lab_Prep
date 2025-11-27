# print("Python", "Java", "c++",  sep=" vs ", end="?") # sep = "," 사이에 sep="vs" 들어감 end="?"끝에 붙여짐
# print("무엇이 더 어려울까?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력 스트림. 정상 메세지, 결과, 로그 등을 보내는 기본통로
# print("Python", "Java", file=sys.stderr) # 표준 에러 스트림. 오류 메시지, 경고, 예외 등 "문제 상황"을 알리는 별도 통로

# 시험 성적표
# scores = {"Max" : 97, "전공실기" :100, "작곡법": 100 }
# for subject, score in scores.items():
#     print(subject, score)
#     print(subject.ljust(4), str(score).rjust(3), sep=":") # ljust=왼쪽 정렬, rjust= 오른쪽 정렬
#

# 은행 대기 순번표
# 001, 002, 003
for num in range(1, 11):
    print("대기 번호 : " +  str(num).zfill(3)) #zfill= 빈칸을 0으로 채우기

# answer = input("당신의 MBTI를 입력하세요")
# print("당신의 mbti는 " + answer + "입니다.")
