def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                value = tokens[col_idx].strip()
                weather_datas.append(float(value))
            except:
                weather_datas.append(0.0)
    return weather_datas

def sumifs(rainfalls, years, selected):
    total = 0
    for i in range(len(rainfalls)):
        if int(years[i]) in selected:
            total += rainfalls[i]
    return total

def main():
    filename = "weather(146)_2001-2022.csv"
    years = get_weather_data(filename, 0)      # 연도는 0번 열
    rainfalls = get_weather_data(filename, 9)  # 강수량은 9번 열

    total_2021 = sumifs(rainfalls, years, [2021])
    total_2022 = sumifs(rainfalls, years, [2022])

    print(f"2021년 총 강수량: {total_2021:.1f}mm")
    print(f"2022년 총 강수량: {total_2022:.1f}mm")
    print(f"2021~2022년 총합: {total_2021 + total_2022:.1f}mm")

if __name__ == "__main__":
    main()
