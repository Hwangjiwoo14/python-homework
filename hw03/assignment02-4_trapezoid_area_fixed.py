upper = int(input("윗변의 길이는?"))
lower = int(input("아랫변의 길이는?"))
height = int(input("높이는?"))

trapezoid_area = ((upper + lower) / 2) * height

print("윗변={}, 아랫변={}, 높이={}일 때".format(upper, lower, height))
print("사다리꼴의 면적은 = {}".format(trapezoid_area))