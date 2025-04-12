def text2lsit(txt):
    text_list = txt.split()
    nums = []
    for word in text_list:
        nums.append(int(num_text))
        print(nums)


def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    print(nums)
    print(sorted(nums))
    sorted_list = sorted(nums)
    return sorted_list[len(nums) // 2]
    return None





def read_text(filename):
    with open(filename) as f:
        text = f.readline()
        print(text)
    # retun "1 2 3 4 5 6 7 "
    return text







def main():
    text = read text("numbers1. txt")
    nums = text2list(text)
    # [10, 5, 3, 7 , 9]
    print(nums)
    print(f"평균값은 {average(nums):.1f}입니다.")
    print(f"중앙값은 {median(nums)}입니다.")


if __name__ == "__main__":
    main()