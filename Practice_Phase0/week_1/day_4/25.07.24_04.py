# 4-1 문자열

sentense = "나는 소년입니다."
print(sentense)
sentense2 = "파이썬은 쉬워요."
print(sentense2)
sentense3 = """
나는 김지수이고,
파이썬은 너무 어려워요
"""
print(sentense3)

sentense4 = "나는 지나가던 나그네이고\n계속 지나갈 것입니다."
print(sentense4)

# 4-2 슬라이싱

jumin = "880120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# Grok 4 Quiz
#Quiz: 주민등록번호 분석기
#문제 설명:
#주민등록번호 문자열(예: "880120-1234567")을 입력받아 슬라이싱으로 다음 정보를 추출하고 판별하는 프로그램을 작성하세요.
#생년월일(연, 월, 일) 추출.
#출생 연도 판별(1900년대 vs. 2000년대, 성별 코드에 따라).
#성별 판별(남성/여성).
#출생 지역 판별(간단히: 서울, 경기, 부산 등 – 뒤 7자리의 2~3번째 숫자 기반).
#모든 정보를 한 번에 출력.
#조건:
#주민등록번호는 항상 "YYMMDD-XXXXXXX" 형식으로 가정(슬라이싱으로 '-' 무시).
#성별 코드(뒤 7자리 첫 번째 숫자): 1/3=남성, 2/4=여성 (1/2=1900년대, 3/4=2000년대).
#지역 코드 예시(뒤 7자리 2~3번째 숫자): 00~08=서울, 09~12=부산, 13~15=인천, 16~25=경기 등(실제 규칙 간단화).
#랜덤 주민번호 생성은 optional( random 모듈 사용 가능).
#출력 예시 (입력: "880120-1234567"):
#생년월일: 1988년 01월 20일
#출생 연도: 1900년대
#성별: 남성
#출생 지역: 서울 (추정)

from random import *

jumin = ""

for i in range(13) :
    number = randint(0,9)
    jumin += str(number)

    print(jumin)
    print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
    print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지

# 4-3 문자열 처리 함수
python = "Python is Amazing"
print(python. lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) #0번쨰 문자가 대문자가 맞는가?
print(len(python)) #몇 글자가 되는가?
print(python.replace("Python", "Java")) # 문자 변화시키기.

index = python.index("n") #n이 몇번째 글자에 있는가?
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("java"))
# print(python.index("java"))
print("hi")

# 4-4 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20) #d는 정수
print("나는 %s을 좋아해요." % "파이썬") # s는 str 문자
print("Apple 은 %c로 시작해요." % "A") # c는 하나의 문자만 출력 (문자 하나만 기대, 강제하고 싶을 때)
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))


# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4
age = 20
color = "red"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 4-5 탈출문자
# \n : 줄바꿈
print("나는 지나가던\n나그네입니다.")

#\" \' : 문장 내에서 따옴표
# 저는 "김지수"입니다.
print('저는 "김지수"입니다.')
print("저는\"김지수\"입니다.")

#\\ : 문장 내에서 \
print("c : \\users\\nanebabo")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 ( 한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

#예) http://naver.com
#규칙 1 : http:// 부분은 제외 => naver.com
#규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

#domain = "http://naver.com"
#print("처음 세자리: " + domain[7:])

#site_name = "naver"
#print()
#print(len(domain)) #글자 갯수

#number = domain.number("e") # 글자 내 'e' 갯수
#print(number)

# print(f"{처음 세자리} + {}")