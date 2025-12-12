import numpy as np
import matplotlib.pyplot as plt

# 1. 극단적인 데이터 생성
# Case A: 아주 작은 소리 (최대 0.1)
y_small = np.random.uniform(-0.1, 0.1, 1000)
# Case B: 아주 큰 소리 (최대 5.0 -> 이미 찢어진 소리 가정)
y_large = np.random.uniform(-5.0, 5.0, 1000)


# 2. 정규화 로직 구현 (Peak Normalization)
def normalize_manual(y, target_level=0.95):
    peak = np.max(np.abs(y))  # 절대값 중 가장 큰 놈(Peak)을 찾음

    # 0으로 나누기 방지 (무음일 경우 원본 반환)
    if peak == 0:
        return y

    return y / peak * target_level  # 전체를 피크로 나누고 타겟 레벨을 곱함


# 적용 (Target을 1.0으로 설정)
y_small_norm = normalize_manual(y_small, 0.95)
y_large_norm = normalize_manual(y_large, 0.95)

# 3. 결과 검증 (Print Proof)
print(f"Small Peak: {np.max(np.abs(y_small)):.2f} -> {np.max(np.abs(y_small_norm)):.2f}")
# 예상: 0.10 -> 1.00
print(f"Large Peak: {np.max(np.abs(y_large)):.2f} -> {np.max(np.abs(y_large_norm)):.2f}")
# 예상: 5.00 -> 1.00

# 4. 시각화 (Visual Proof)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# 작은 소리 비교
ax[0].plot(y_small, label="Original (Small)", alpha=0.5)
ax[0].plot(y_small_norm, label="Normalized", alpha=0.5)
ax[0].set_ylim(-1.5, 1.5)
ax[0].set_title("Small Audio Normalization")
ax[0].legend()

# 큰 소리 비교
ax[1].plot(y_large, label="Original (Large)", alpha=0.5)
ax[1].plot(y_large_norm, label="Normalized", alpha=0.5)
ax[1].set_ylim(-6.0, 6.0)
ax[1].set_title("Large Audio Normalization")
ax[1].legend()

plt.tight_layout()
plt.show()