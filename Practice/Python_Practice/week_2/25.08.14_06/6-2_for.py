#6-2 for

# for waiting_no in[0, 1, 2, 3, 4,]:
#     print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6): # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

Megacoffee = ["김지수", "이희빈", "김준호"]
for customer in Megacoffee:
    print("{0},커피가 준비되었습니다.".format(customer)) # {0}은 문자열 안 값이 들어갈 위치를 지정
    #.format()은 문자열의 내장 메서드로, 중괄호{} 자리에 값을 매칭시켜 넣어준다.
name = "지수"
drink = "아메리카노"
print("{0}님, {1}가 준비되었습니다.".format(name, drink))
