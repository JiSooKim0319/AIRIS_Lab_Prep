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

# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송. 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도는 {2}]"
        .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

    def scenario(self, attack_location=None, damage_list=None, flying_location=None):
        if attack_location is not None:
            self.attack(attack_location)
        if flying_location is not None:
            self.fly(self.name, flying_location)
        if damage_list:
            for d in damage_list: # for d in 이 있기에 10의 데미지 값을 계산 후 20 데미지 값을 계산 하는 것. 반복문
                self.damaged(d)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 15, 10)
valkyrie.scenario(attack_location=3, flying_location=3, damage_list=[10, 20, 50])