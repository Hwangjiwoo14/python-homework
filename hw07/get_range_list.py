def get_range_list(n):
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i = i + 1
    return result

def main():
    n = 5
    numbers = get_range_list(n)
    print(f"1부터 {n}까지의 리스트: {numbers}")

if __name__ == "__main__":
    main()
