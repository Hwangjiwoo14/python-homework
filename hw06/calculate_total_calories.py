def calculate_total_calories(fruit_cal, fruit_eat):
    total = 0
    for item in fruit_eat:
        calorie = fruit_cal[item] * fruit_eat[item]
        print(f"{item}: {fruit_cal[item]} kcal/g * {fruit_eat[item]}g = {calorie:.2f} kcal")
        total += calorie
    return total

def main():
    fruit_cal = {
        "한라봉": 50/100,
        "딸기": 34/100,
        "바나나": 77/100,
    }

    fruit_eat = {
        "한라봉": 150,
        "딸기": 200,
        "바나나": 100,
    }

    total_calories = calculate_total_calories(fruit_cal, fruit_eat)
    print(f"\n총 칼로리는 {total_calories:.2f} kcal입니다.")

if __name__ == "__main__":
    main()
