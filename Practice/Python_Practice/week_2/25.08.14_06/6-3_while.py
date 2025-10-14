#6-3_while

# customer = "김지수"
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("마감입니다") # or break

customer = "이희빈"
person = "사람"

while person != customer: #("!="은 비교 연산자 중 하나로 같지 않다. "=="은 같다)
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?") # input은 사용자로 부터 키보드로 입력을 받아 문자열로 person 변수에 저장.