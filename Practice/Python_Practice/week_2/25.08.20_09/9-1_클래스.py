# # 마린 : 공격 유닛, 군인. 총을 쏫 수 있음
# name = "마린"
# hp = 40
# damage = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# tank_name = "탱크"
# tank_hp = "150"
# tank_damage = "35"
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = "150"
# tank2_damage = "35"
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
#
# attack(name, 1, damage)
# attack(tank_name, 2, tank_damage)

class unit:
    def __init__(self, name, hp, damage):
         self.name = name
         self.hp = hp
         self.damage = damage
         print("{0} 유닛이 생성되었습니다.".format(self.name))
         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = unit("마린", 40, 5)
tank1 = unit("탱크", 150, 35)


