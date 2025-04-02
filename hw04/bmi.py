#height = 163
height = int(input("키가 얼마인가요? (cm): "))
#weight = 47
weight = int(input("몸무게가 얼마인가요? (kg): "))

height_m = height / 100

bmi = weight / pow(height_m, 2)
print("키: {}cm, 몸무게: {}kg, BMI: {:.2f}".format(height, weight, bmi))
