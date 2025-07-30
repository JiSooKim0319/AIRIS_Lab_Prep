# 5-2 사전

cabinet = {3:"김지수", 100:"민윤지"}
#print(cabinet[3])
#print(cabinet[100])

#print(cabinet.get(100))
#print(cabinet[5])
#print(cabinet.get(5))
#print(cabinet.get(5,"사용가능"))
#print("보고싶다")

#print(3 in cabinet)
#print(5 in cabinet)

cabinet = {"A-3":"민윤지", "B-100":"박근호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "이희빈"
cabinet["B-100"] = "김준호"
print(cabinet)

#간 손님  
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)