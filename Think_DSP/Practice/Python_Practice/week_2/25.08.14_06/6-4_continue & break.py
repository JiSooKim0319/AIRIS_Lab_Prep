absent = [2,5]# 결석
no_book = [7] # 책을 깜빡함
for student in range(1, 11) : # 1, 2, 3, 4, 5, 6, ----
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}은 교무실로 따라와라".format(student))
        break
    else:
        print("{0}, 책 읽어보자.".format(student)) #else가 없었기에 처음 인풋 아웃풋으로 송출안됨
