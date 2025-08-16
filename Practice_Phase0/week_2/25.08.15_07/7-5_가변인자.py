#7-5 가변인자
from multiprocessing.util import MAXFD

from PIL.MspImagePlugin import MspDecoder


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5 )
#
# profile("이희빈", 20, "python", "Java", "Java", "Java", "Java")
# profile("김준호", 25, "java", "MAX", "", "", "")

def profile(name, age, *language): #가변 인수
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in language : # for = 반복할 대상이 있을 때 그 대상의 원소를 하나씩 꺼내며 같은 코드를 반복 실행할 떄 사용
        print(lang, end=" ")
    print() # 줄바꿈 수행. 앞에 end=""때문에 줄이 바뀌지 않기에 새 줄에서 다음 사람 새로운 출력

profile("이희빈", 20, "python", "Java", "Java", "Java", "Java", "LOL")
profile("김준호", 25, "java", "MAX", )

