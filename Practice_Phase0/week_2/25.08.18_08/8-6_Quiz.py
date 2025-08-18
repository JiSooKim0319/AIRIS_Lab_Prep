# Quiz) 당신의 회사에서는 매주 1회 작생해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
from fileinput import filename

# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 "1주차.txt, "2주차.txt", ...와 같이 만듭니다.

# for num in range(1, 51):
#     print(" - " + str(num) + "주차 주간 보고 - ")
#     print("부서 :")
#     print("이름 :")
#     print("업무 요약 : ")
#     print()
#
#     filename = f"{num}주차.txt"
#
#     content = (
#         f"- {num} 주차 주간 보고 -\n"
#         "부서 : \n"
#         "이름 : \n"
#         "업무 요약 :\n"
#     )
#     with open(filename,"w", encoding="utf-8" ) as file:
#         file.write(content)


for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n 부서:")
        report_file.write("\n 이름:")
        report_file.write("\n 업무 요약:")