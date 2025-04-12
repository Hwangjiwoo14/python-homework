def text2list(txt):
    text_list = txt.split()
    nums = []
    for word in text_list:
        nums.append(int(word))
    return nums

def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    sorted_list = sorted(nums)
    count = len(sorted_list)

    if count % 2 == 0:
        first = sorted_list[count // 2 - 1]
        second = sorted_list[count // 2]
        return (first + second) / 2
    else:
        return sorted_list[count // 2]

def read_text(filename):
    with open(filename) as f:
        text = f.readlines()
    return text

def main():
    filename = "numbers2.txt"
    lines = read_text(filename)

    nums = []
    for line in lines:
        nums.extend(text2list(line.strip()))

    print("총 숫자의 개수:", len(nums))
    print("평균값: {:.1f}".format(average(nums)))
    print("최댓값:", max(nums))
    print("최솟값:", min(nums))
    print("중앙값:", median(nums))

if __name__ == "__main__":
    main()

