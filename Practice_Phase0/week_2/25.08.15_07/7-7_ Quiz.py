#Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# 표준 체중 : 각 개인의 키에 적당한 체중

#(성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
           # 함수명 : std_weight
           # 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

#( 출력 예제 )
# 키 175cm 남자의 표준 체중은 67.38kg

# def std_weight(height, gender):
#     std_weight_m = height * height * 22
#     print("키 {1}cm {2}의 표준 체중은 {0}kg.".format(std_weight_m, height, gender))
#     return std_weight_m
#
# std_weight(1.70, "남자" )
#
# def std_weight(height, gender):
#     std_weight_w = height * height * 21
#     print("키 {1}cm {2}의 표준 체중은 {0}kg.".format(std_weight_w, height, gender))
#     return std_weight
#
# std_weight(1.63, "여자" )
############### 김지수 방식 ####################

# GPT-5 문제 풀이

def std_weight(height_cm, gender):
    height_m = height_cm /100
    if gender == "M":
        value = height_m * height_m * 22
    elif gender == "F":
        value = height_m * height_m * 21
    else:
        raise ValueError("gender must be 'M' or 'F'")
    return value

h1, g1 = 171, "M"
w1 = std_weight(h1, g1)
print(f"키 {h1}cm {g1}의 표준 체중은 {w1:.2f}kg")

h2, g2 = 159, "F"
w2 = std_weight(h2, g2)
print(f"키 {h2}cm {g2}의 표준 체중은 {w2:.2f}kg")
