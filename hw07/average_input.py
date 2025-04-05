def average(nums):
    total = 0
    count = 0
    for num in nums:
        total = total + num
        count = count + 1
    return total / count


def main():
    input_text = input("숫자들을 입력하세요 (예: 10, 20, 30): ")

    tokens = input_text.split()

    nums = []

    for item in tokens:
        # 쉼표가 있다면 지워준다
        cleaned = ""
        i = 0
        while i < len(item):
            if item[i] != ",":
                cleaned = cleaned + item[i]
            i = i + 1
        nums.append(int(cleaned))

    avg = average(nums)
    print(f"입력한 숫자들의 평균은 {avg:.2f}입니다.")


if __name__ == "__main__":
    main()
