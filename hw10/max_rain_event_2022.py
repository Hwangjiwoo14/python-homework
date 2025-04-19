def get_weather_data(fname, rain_col):
    rainfalls = []
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                rain = float(tokens[rain_col].strip())
                rainfalls.append(rain)
            except:
                rainfalls.append(0.0)
    return rainfalls

def get_max_rain_event(rainfalls):
    max_event_total = 0.0
    current_event_total = 0.0

    for rain in rainfalls:
        if rain > 0:
            current_event_total += rain
        else:
            if current_event_total > max_event_total:
                max_event_total = current_event_total
            current_event_total = 0.0

    if current_event_total > max_event_total:
        max_event_total = current_event_total

    return max_event_total

def main():
    filename = "weather(146)_2022-2022.csv"
    rain_col = 9

    rainfalls = get_weather_data(filename, rain_col)
    max_event_rainfall = get_max_rain_event(rainfalls)

    print(f"2022년 강우 이벤트 중 최대 강수량은 {max_event_rainfall:.1f}mm입니다.")

if __name__ == "__main__":
    main()
