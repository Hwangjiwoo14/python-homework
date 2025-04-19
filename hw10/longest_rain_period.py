def get_weather_data(fname, year_col, rain_col):
    years = []
    rainfalls = []
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                year = int(float(tokens[year_col].strip()))
                rain = float(tokens[rain_col].strip())
                years.append(year)
                rainfalls.append(rain)
            except:
                continue
    return years, rainfalls

def get_max_rain_streak(years, rainfalls, target_year):
    max_streak = 0
    current_streak = 0

    for i in range(len(years)):
        if years[i] == target_year:
            if rainfalls[i] > 0:
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                current_streak = 0
    return max_streak

def main():
    filename = "weather(146)_2001-2022.csv"
    year_col = 0
    rain_col = 9  

    years, rainfalls = get_weather_data(filename, year_col, rain_col)
    max_streak_2022 = get_max_rain_streak(years, rainfalls, 2022)

    print(f"2022년 최장 연속 강우일수는 {max_streak_2022}일입니다.")

if __name__ == "__main__":
    main()
