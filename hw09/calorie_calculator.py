def read_db(filename):
    calorie_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            if len(tokens) >= 2:
                food = tokens[0]
                try:
                    cal_per_100g = float(tokens[1])  # 100g당 칼로리
                    calorie_dic[food] = cal_per_100g
                except ValueError:
                    print(f"칼로리 값 오류: {tokens[1]} (음식: {food})")
    return calorie_dic


def main():
    calorie_db = read_db("calorie_db.csv")

    food_eaten = {
        "한라봉": 150,
        "딸기": 200,
        "바나나": 120,
    }

    total_cal = 0
    print("섭취 칼로리 계산 결과:\n")
    print(f"{'음식명':<10} {'섭취량(g)':<10} {'단위칼로리(kcal/100g)':<20} {'총 칼로리(kcal)':<15}")

    for food, gram in food_eaten.items():
        if food in calorie_db:
            cal_per_100g = calorie_db[food]
            cal = gram * (cal_per_100g / 100)
            total_cal += cal
            print(f"{food:<10} {gram:<10} {cal_per_100g:<20} {cal:<15.2f}")
        else:
            print(f"{food:<10} {gram:<10} {'데이터 없음':<20} {'-':<15}")

    print(f"\n총 섭취 칼로리는 {total_cal:.2f} kcal 입니다.")


if __name__ == "__main__":
    main()
