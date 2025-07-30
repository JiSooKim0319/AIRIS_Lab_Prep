# 5-4 세트

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

marry = {"윤지", "박호", "박소"}
now = set(["윤지", "주영"])

# 교집합 ( marry 와 now 을 모두 할 수 있는 사람)
print( marry & now)
print(marry.intersection(now))

# 합집합 (marry 할 수 있거나 now 할 수 있는 개발자)
print(marry | now)
print(marry.union(now))

# 차집합 (marry 할 수 있지만 now 는 안 되는 사람)
print(marry - now)
print(marry.difference(now))

# marry 할 수 있는 사람이 늘어남
marry.add("영비")
print(marry)

# marry에 빠졌어요
marry.remove("박소")
print(marry)