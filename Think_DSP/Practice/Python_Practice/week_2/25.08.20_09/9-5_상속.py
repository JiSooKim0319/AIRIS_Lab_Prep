class Unit: # 클래스란 무엇인가. 같은 구조와 동작을 가진 데이터 뭉치를 찍어내기 위한 형(예_붕어빵 틀)
    def __init__(self, name, hp): #__init__ (initializer 약자) 새 객체가 생성될 때 마다 자동으로 호출 되어 "초기 상태 설정"
         self.name = name
         self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage


    def attack(self, location):
        print(
            "{0} : {1}시 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage)
        )

    def damaged(self, damage):
        print(
            "{0} : {1} 데미지를 받았습니다."
              .format(self.name, damage)
        )
        self.hp -= damage
        print(
            "{0} : 남은 체력은 {1}입니다."
              .format(self.name, self.hp)
        )
        if self.hp <= 0:
           print("{0} : 파괴되었습니다.".format(self.name))

firebat = AttackUnit("파이어뱃", 100, 20)
firebat.attack(5)

firebat.damaged(25)
firebat.damaged(25)
firebat.damaged(25)
firebat.damaged(25)
