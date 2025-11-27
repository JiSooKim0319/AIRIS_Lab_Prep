class Unit: # 클래스란 무엇인가. 같은 구조와 동작을 가진 데이터 뭉치를 찍어내기 위한 형(예_붕어빵 틀)
    def __init__(self, name, hp, damage): #__init__ (initializer 약자) 새 객체가 생성될 때 마다 자동으로 호출 되어 "초기 상태 설정"
         self.name = name
         self.hp = hp
         self.damage = damage
         print("{0} 유닛이 생성되었습니다.".format(self.name))
         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) # marine= 객체(object) instance
# tank1 = Unit("탱크", 150, 35)

#레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음) 즉 == 체력이 안보여야 함.
wraith1 = Unit("레이스", 80, 5)
print("{0} 유닛이 생성되었습니다.".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음) 즉 == 새로운 기술 추가
wraith2 = Unit("빼았은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
