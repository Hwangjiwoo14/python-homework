def is_leap_year(y):
    if y % 4 != 0:
        return False
    else:
        if y % 100 == 0:
            return False
        else:
            return True

def main():
    year = 2024
    result = is_leap_year(year)
    print(f"{year}년은 윤년인가요? {result}")

if __name__ == "__main__":
    main()
