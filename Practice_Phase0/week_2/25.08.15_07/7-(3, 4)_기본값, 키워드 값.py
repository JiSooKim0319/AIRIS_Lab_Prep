# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
#           .format(name, age, main_lang))
#
# profile("이희빈", "26", "none")
# profile("김준호", "26", "none")

# 같은 학교 같은 학년 같은 반 수업

# def profile(name, age=26, main_lang="none" ):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어{2}"
#           .format(name, age, main_lang))
#
# profile("이희빈")
# profile("김준호")


# 7-4 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="이희빈", main_lang="python", age="26")
profile(main_lang="Java", name="김준호", age="26")

