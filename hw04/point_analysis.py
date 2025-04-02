import math

x1 = int(input("첫 번째 점의 x 좌표를 입력하세요: "))
y1 = int(input("첫 번째 점의 y 좌표를 입력하세요: "))
x2 = int(input("두 번째 점의 x 좌표를 입력하세요: "))
y2 = int(input("두 번째 점의 y 좌표를 입력하세요: "))

if x1 > 0 and y1 > 0:
    print("첫 번째 점은 1사분면입니다.")
elif x1 < 0 and y1 > 0:
    print("첫 번째 점은 2사분면입니다.")
elif x1 < 0 and y1 < 0:
    print("첫 번째 점은 3사분면입니다.")
elif x1 > 0 and y1 < 0:
    print("첫 번째 점은 4사분면입니다.")
elif x1 == 0 and y1 != 0:
    print("첫 번째 점은 y축 위에 있습니다.")
elif x1 != 0 and y1 == 0:
    print("첫 번째 점은 x축 위에 있습니다.")
else:
    print("첫 번째 점은 원점입니다.")

if x2 > 0 and y2 > 0:
    print("두 번째 점은 1사분면입니다.")
elif x2 < 0 and y2 > 0:
    print("두 번째 점은 2사분면입니다.")
elif x2 < 0 and y2 < 0:
    print("두 번째 점은 3사분면입니다.")
elif x2 > 0 and y2 < 0:
    print("두 번째 점은 4사분면입니다.")
elif x2 == 0 and y2 != 0:
    print("두 번째 점은 y축 위에 있습니다.")
elif x2 != 0 and y2 == 0:
    print("두 번째 점은 x축 위에 있습니다.")
else:
    print("두 번째 점은 원점입니다.")

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance > 1:
    print("두 점 사이의 거리가 1보다 큽니다.")
elif distance == 1:
    print("두 점 사이의 거리가 1입니다.")
else:
    print("두 점 사이의 거리가 1보다 작습니다.")

print(f"두 점 사이의 거리는 {distance:.3f}입니다.")