# def 이해하기.

# 1) 입력도 없고 반환값도 없는 함수
# def 함수명() :
#   수행문장
#   ....
def fun1():
    print('hello')

fun1()
fun1()
fun1()

# 2) 입력만 있는 함수
# def 함수명(매개변수1, 매개변수2,...)
#   수행문장
def fun2(a,b):
    print(f'{a} * {b} = {a*b}')

fun2(1,2)
fun2(4,5)

# 3) 반환값만 있는 함수
# def 함수명()
#   수행문장
#   return 반환값
def fun3():
    return "이희빈"

a = fun3()
print(a + " 바보")

# 4) 입력, 반환값이 둘다 있는 함수
# def 함수명(매개변수1, 매개변수2,...)
#   수행문장
#   return 반환값

def fun4(a, b):
    return a * b

c = fun4(4, 5)
print(c * 4)

# 5) 예제 만들기 (구구단)
def gugudan(num):
    for i in range(1, 10):
        print(f'{num} * {i} = {num * i}')

# 구구단 출력
gugudan(1)
gugudan(2)
gugudan(3)
gugudan(4)

# 6) 함수 응용(디폴트 매개변수, 매개변수 N개, 튜플 반환)

# 6-1)디폴트 매개변수
def fun5(a, b=5, c=10):
    return a + b + c

fun5(1, 2, 3) # 1 + 2 + 3
fun5(1,2)        # 1 + 2 + 10
fun5(1)                # 1 + 5 + 10

# 디폴트 파라미터는 앞에서만 사용하면 오류 남
# 인수가 비었을 때 판단이 가능함.
# def fun6(a=10, b):
#     return a + b
#
# fun6(1, 2)

# 6-2) 매개변수 N개
# 예재
def func6(*args):
    # *args : 이 함수는 몇 개의 숫자를 받든 모두 튜플로 묶어 args에 저장합니다.
    a = 0  # 덧셈 결과를 저장할 변수 a를 0으로 초기화

    for i in args:  # args(튜플) 안의 값들을 하나씩 꺼내서 (i) 반복합니다.
        a = a + i  # 꺼낸 i를 변수 a에 계속 더합니다.

    return a  # 최종 합계 a를 함수 밖으로 반환(돌려줌)합니다.

c = func6(2,3,4,5,6)
print(c)


# 7) 문제1 : 두 숫자의 합과 곱 계산기
# 두 개의 숫자를 입력받아(매개변수) 그들의 **합(더하기 결과)**과 **곱(곱하기 결과)**을 모두 계산한 후,
# 이 두 결과를 **반환(return)**하는 함수를 만들어 보세요.

def calculate_sum_and_product(num1, num2):
    return (num1+num2, num1*num2)
d = calculate_sum_and_product(1,2)
print(d)

# 7-1) 문제 2 : 합격/불합격 판별 및 점수 평균 계산기
# 여러 과목의 점수들을 입력받아 합격 여부를 판별하고, 이 점수들의 평균을 계산하여 반환하는 함수를 만들어 보세요.
# 🌟 요구사항함수
# 이름: $\text{check_pass_and_average}$로 정해봅시다.
# 매개변수: 몇 개의 점수가 입력될지 모르므로, **$\text{*args}$**를 사용해 N개의 점수(숫자)를 받도록 정의하세요.
# 수행문장 (로직):합격 기준: 입력된 모든 점수가 60점 이상이어야만 '합격'입니다. 점수 중 단 하나라도 60점 미만이면 '불합격'입니다.
# 평균 계산: 입력된 모든 점수의 평균을 계산합니다.
# 반환값:합격 여부를 나타내는 문자열 (예: "합격" 또는 "불합격")계산된 평균 점수 (소수점일 수 있습니다)

def check_pass_and_average(*args):
    if not args:
        return "점수 없음"

    for score in args:
        if score < 60:
            total_score = sum(args)
            average_score = total_score / len(args)
            return "불합격", average_score

    total_score = sum(args)
    average_score = total_score / len(args)
    return "합격", average_score

result1, average1 = check_pass_and_average(70,80,93)
print(f"결과 1: {result1}, 평균 1: {average1:.2f}")

result2, average2 = check_pass_and_average(70,53,92)
print(f"결과 2: {result2}, 평균 2: {average2:.2f}")

