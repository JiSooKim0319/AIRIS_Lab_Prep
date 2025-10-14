class Unit: # 클래스란 무엇인가. 같은 구조와 동작을 가진 데이터 뭉치를 찍어내기 위한 형(예_붕어빵 틀)
    def __init__(self, name, hp, damage): #__init__ (initializer 약자) 새 객체가 생성될 때 마다 자동으로 호출 되어 "초기 상태 설정"
         self.name = name
         self.hp = hp
         self.damage = damage
         print("{0} 유닛이 생성되었습니다.".format(self.name))
         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # marine= 객체(object) instance
tank1 = Unit("탱크", 150, 35)
