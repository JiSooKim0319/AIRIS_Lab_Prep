# def open_account():
#      print("새로운 계좌가 생성되었습니다.")

# 7-2 전달값과 변환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0} 원입니다.".format(balance + money)) # 더하기는 하나의 값 즉 계산의 결과를 보여주기 위한 연산
    return balance + money

balance = 0
balance = deposit(balance, 1000)

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많음면
        print("출금이 완료되었습니다. 잔액은{0}입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

balance = withdraw(balance, 500)

def withdraw_night(balance, money): # 저녁에 출금 + 수수료
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

money = 2000
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원 이고, 출금 금액은 {2}원 입니다.".format(balance, commission, money))

