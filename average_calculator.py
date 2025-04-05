def average(nums):
    total = 0
    index = 0

    while index < 5:
        total = total + nums[index]
        index = index + 1

    return total / 5

def main():
    numbers = [10, 20, 30, 40, 50]
    avg = average(numbers)
    print(f"리스트 {numbers}의 평균은 {avg:.2f}입니다.")

if __name__ == "__main__":
    main()
