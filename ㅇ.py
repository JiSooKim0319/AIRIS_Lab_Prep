from PIL import Image, ImageDraw
import math

# XP Dog 스타일 캐릭터 제작
frames = []
size = (800, 600)

for frame in range(48):  # 48프레임 (부드러운 애니메이션)
    img = Image.new('RGB', size, color='lightblue')  # XP 배경색
    draw = ImageDraw.Draw(img)

    # 개 몸체 (노란색, 픽셀 스타일)
    draw.rectangle([250, 250, 400, 400], fill='yellow', outline='orange', width=2)

    # 개 머리 (원)
    draw.ellipse([300, 180, 450, 280], fill='yellow', outline='orange', width=2)

    # 눈 (검은 픽셀)
    draw.rectangle([330, 210, 340, 220], fill='black')  # 왼쪽 눈
    draw.rectangle([390, 210, 400, 220], fill='black')  # 오른쪽 눈

    # 책 (손에 들고 있는 형태)
    book_angle = math.sin(frame / 48 * math.pi * 2) * 5  # 살짝 회전
    draw.rectangle([420, 300, 500, 380], fill='red', outline='darkred', width=2)
    draw.line([460, 300, 460, 380], fill='darkred', width=1)  # 책 중앙선

    # 텍스트
    draw.text((250, 450), "FOCUS MODE", fill='black')

    frames.append(img)

# GIF 저장
frames[0].save('xp_dog_focus.gif', save_all=True, duration=100, loop=0)
