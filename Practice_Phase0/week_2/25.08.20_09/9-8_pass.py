from music21.figuredBass.rules import specialResDoc


class Unit: # 클래스란 무엇인가. 같은 구조와 동작을 가진 데이터 뭉치를 찍어내기 위한 형(예_붕어빵 틀)
    def __init__(self, name, hp, speed): #__init__ (initializer 약자) 새 객체가 생성될 때 마다 자동으로 호출 되어 "초기 상태 설정"
         self.name = name
         self.hp = hp
         self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed)
              )

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# Pass
# def game_start():
#     print("게임이 시작됩니다.")
#
# def game_end():
#     print("게임이 종료됩니다.")
#     pass
#
# game_start()
# game_end()

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super은 다중 상속 시 맨 앞 부모만 가져올 수 있음.
                                             # 그렇기에 두 가지 이상의 상속을 받으려면 Unit. Flyable __init__ 따로 생성 해야 함.
        self.location = location