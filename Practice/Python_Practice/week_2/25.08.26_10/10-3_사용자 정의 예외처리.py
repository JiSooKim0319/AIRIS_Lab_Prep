class BigNumberError(Exception): #한 자릿 수 이상시 오류(특정한 상황). #ValueError는 큰 폭에 오류설정
    def __init__(self, msg): # 학생증 만들기. 이름을 접수해서 학생증에 기록(self.msg)해 둔다.
        self.msg = msg

    def __str__(self): #
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >=10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)