def get_weather_data_float(fname, col_idx):
    data = []
    with open(fname, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                value = float(tokens[col_idx])
                data.append(value)
            except:
                continue
    return data


def count_rain_over_5mm(nums):
    count = 0
    for x in nums:
        if x >= 5.0:  
            count += 1
    return count


def main():
    filename = "weather(146)_2020-2020.csv"
    rainfalls = get_weather_data_float(filename, 9)

    days_over_5mm = count_rain_over_5mm(rainfalls)

    with open("result_2020_rain_over_5mm.txt", "w", encoding="utf-8") as fout:
        fout.write(f"2020년 5mm 이상 강우일수: {days_over_5mm}일\n")


if __name__ == "__main__":
    main()
