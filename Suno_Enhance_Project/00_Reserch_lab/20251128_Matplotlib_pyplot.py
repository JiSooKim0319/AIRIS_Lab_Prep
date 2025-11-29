import matplotlib.pyplot as plt

# 1. 캔버스와 칸 준비
# figsize=(10, 4) : 가로 10인치, 세로 4인치 (오디오는 옆으로 기니까 가로로 길게)
fig, ax = plt.subplots(figsize=(10, 4))

# 2. 이름표 붙이기
ax.set_title("My Audio Analysis")
ax.set_xlabel("Time (s)")       # 가로축 이름
ax.set_ylabel("Frequency (Hz)") # 세로축 이름

# 3. (나중에 여기에 그림 그리는 코드가 들어갑니다)
# ...

# 4. 마무리 정돈 (필수!)
# 글자가 그림 밖으로 삐져나가지 않게 여백을 딱 맞춰줍니다.
fig.tight_layout()

# 5. 확인하기
plt.show()
# (나중에는 plt.show() 대신 fig.savefig()로 저장할 겁니다)
    # `show()`:** 지금 당장 눈으로 확인하고 창을 닫을 때 (연습용).
    # `savefig()`:** 밤새 컴퓨터가 알아서 100장의 이미지를 파일로 저장하게 시킬 때 (실전용).
