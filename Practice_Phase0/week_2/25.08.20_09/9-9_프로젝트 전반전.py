class Unit: # 클래스란 무엇인가. 같은 구조와 동작을 가진 데이터 뭉치를 찍어내기 위한 형(예_붕어빵 틀)
    def __init__(self, name, hp, speed): #__init__ (initializer 약자) 새 객체가 생성될 때 마다 자동으로 호출 되어 "초기 상태 설정"
         self.name = name
         self.hp = hp
         self.speed = speed
         print("{0} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed)
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

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(
            "{0} : {1}시 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage)
        )
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못 합니다.".format(self.name))
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 업그레이드 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False: # false에 false => True
            return
    # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환됩니다."
              .format(self.name))
            self.damage *= 2
            self.seize_mode = True
    # 현재 시즈 모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드가 해제됩니다."
                  .format(self.name))
            self.damage /= 2
            self.seize_mode = False

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

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloked = False

    def clocking(self):
        if self.cloked == True :
            print("{0} : 클로킹 모드를 해제 합니다.".format(self.name))
            self.cloked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.cloked = True

