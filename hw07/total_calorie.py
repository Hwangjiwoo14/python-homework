def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:
        gram = fruits[fruit]
        cal_per_gram = fruits_calorie_dic[fruit] / 100
        cal = gram * cal_per_gram
        print(f"{fruit}: {fruits_calorie_dic[fruit]} kcal/100g * {gram}g = {cal:.2f} kcal")
        total = total + cal
    return total


def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}

    total = total_calorie(fruits, fruits_calorie_dic)
    print(f"\n총 칼로리는 {total:.2f} kcal입니다.")


if __name__ == "__main__":
    main()