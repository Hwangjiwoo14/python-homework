import math

print(f"{'각(°)':<5} {'라디안':<10} {'sin':<10} {'cos':<10} {'tan'}")
print("=" * 45)

for degree in range(11):  # 0°부터 10°까지
    radian = math.radians(degree)
    sine = math.sin(radian)
    cosine = math.cos(radian)
    tangent = math.tan(radian)

    print(f"{degree:<5} {radian:<10.4f} {sine:<10.4f} {cosine:<10.4f} {tangent:.4f}")