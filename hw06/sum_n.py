def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("1부터 n까지의 합을 구할 숫자 n을 입력하세요: "))
print("1부터", n, "까지의 합은", sum_n(n), "입니다.")
