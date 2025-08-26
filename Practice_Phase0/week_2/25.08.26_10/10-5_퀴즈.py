# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# 출력 메시지 : "잘못 된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다.

#[코드]
class SoldOutError(Exception):
    pass
chinken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}].".format(chinken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chinken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print(" [대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chinken -= order
        if chinken == 0:
         raise SoldOutError
    except ValueError:
        print("잘못 된 값을 입력하였습니다.")
    except SoldOutError:
        print("출력 메시지 : 재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
