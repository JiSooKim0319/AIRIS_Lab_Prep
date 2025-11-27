# 5-5 자료구조의 변경
# 커피숍
menu = {"아아", "바치케", "마카롱"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))