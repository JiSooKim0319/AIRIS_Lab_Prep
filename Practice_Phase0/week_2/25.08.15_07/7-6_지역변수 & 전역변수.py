gun = 10

# def checkpoint(soldier): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldier
#     print("[함수 내] 남은 총 : {0}". format(gun))

def checkpoint_ret(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #밖으로 전달

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))