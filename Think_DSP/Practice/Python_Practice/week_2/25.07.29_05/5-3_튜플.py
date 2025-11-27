# 5-3 튜플

menu = ("삼겹살", "쌈 채소")
print(menu[0])
print(menu[1])

#menu.add("밥") X 안됨. -> 고정된 값만 사용 가능

# name = "김지수"
# age = "26"
# hobby = "성장"
# print(name, age, hobby)

(name, age, hobby) = ( "김지수", "26", "성장")
print(name, age, hobby)