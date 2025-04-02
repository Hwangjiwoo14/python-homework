height = int(input("키가 얼마인가요? (cm): "))
weight = int(input("몸무게가 얼마인가요? (kg): "))

height_m = height / 100
bmi = weight / pow(height_m, 2)

if bmi >= 23 and bmi < 25:
    print("1단계 비만입니다.")
elif bmi >= 25 and bmi < 30:
    print("1단계 비만입니다.")
elif 30 <= bmi and bmi < 35:
# elif 30 <= bmi < 35:
    print("2단계 비만입니다.")
elif bmi >= 35:
    print("3단계 비만입니다.")

if bmi >= 35:
    obesity_level = "3단계 비만"
elif bmi >= 30:
    obesity_level = "2단계 비만"
elif bmi >= 25:
    obesity_level = "1단계 비만"
elif bmi >= 23:
    obesity_level = "비만 전단계"
else:
    obesity_level = "정상 이하"  # 기존 기준에 따르면 정상 범위보다 낮음

print("키: {}cm, 몸무게: {}kg, BMI: {:.2f}".format(height, weight, bmi))
print("당신의 비만 정도는 '{}'입니다.".format(obesity_level))