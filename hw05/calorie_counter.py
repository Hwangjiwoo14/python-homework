fruit_cal = {
    "한라봉": 50 / 100,
    "딸기": 34 / 100,
    "바나나": 77 / 100,
}

fruit_eat = {
    "한라봉": 150,
    "딸기": 200,
    "바나나": 100,
}

fruit_eat_list = ["한라봉", "딸기", "바나나"]

total = 0
for item in fruit_eat_list:
    cal = fruit_cal[item] * fruit_eat[item]
    print(f"{item}: {fruit_cal[item]} * {fruit_eat[item]} = {cal} kcal")
    total += cal

print(f"총 칼로리는 {total:.2f} kcal입니다.")