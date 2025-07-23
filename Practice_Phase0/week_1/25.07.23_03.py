# 3-2 간단한 수식
print(2 + 3 * 4) #14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4
print(number)

number = number + 2
print(number) # 16

number += 1
print(number)
number -= 1
print(number)

number *= 2
print(number)

number /= 2
print(number)

# 생각정리_ 파이썬 코드는 위에서 아래로 한 줄씩 순차적으로 실행 됨,
# 컴퓨터 메모리에 저장되어, 이전 상태를 기반으로 업데이트 되는 원리.

# 3-3 숫자 처리 함수
print(abs(-5)) # 절대값
print(pow(4, 2)) # 제곱값
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최솟값
print(round(3.14)) # 반올림

from math import *
print(floor(3.14)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(9)) # 제곱근

# 3-4 랜덤함수
from random import *

print(random() * 10) # 0.0 - 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 - 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 - 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 - 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1- 45 이하의 임의의 값 생성

# 3-5 퀴즈

#Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

#조건1 : 랜덤으로 날짜를 뽑아야 함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건3 : 매월 1-3일은 스터디 준비를 해야 하므로 제회

#(출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.

from random import *
# date =  print(randint(4, 28 )) #이것이 틀린점 print는 보여주기만 가능, 즉 저장 및 반환이 되지 않음.
# print(f"오프라인 스터디 모임 날짜는 매월 {date} 일로 선정되었습니다.")


#정답.
from random import *  # random 모듈 불러오기 (randint 함수 사용 가능)
date = randint(4, 28)  # 랜덤으로 4~28 사이 숫자 생성하고 date에 저장
print(f"오프라인 스터디 모임 날짜는 매월 {date} 일로 선정되었습니다.")  # f-string으로 출력
