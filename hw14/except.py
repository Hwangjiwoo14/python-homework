def main_input_numbers():
    numbers = []

    while True:
        user_input = input("X=? ")

        if user_input == "-1":
            break

        try:
            value = int(user_input)
            if value > 0:
                numbers.append(value)
        except ValueError:
            continue

    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"입력된 값은 {numbers} 입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다.")
    else:
        print("입력된 자연수가 없습니다.")

if __name__ == "__main__":
    main_input_numbers()
