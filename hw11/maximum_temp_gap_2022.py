def get_weather_data(fname):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            tmax = float(tokens[3])
            tavg = float(tokens[4])
            tmin = float(tokens[5])
            rain = float(tokens[6])
            weather_datas.append([year, month, day, tmax, tavg, tmin, rain])
    return weather_datas


def maximum_temp_gap(dates, tmax, tmin):
    max_gap = tmax[0] - tmin[0]
    max_gap_date = dates[0]

    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if gap > max_gap:
            max_gap = gap
            max_gap_date = dates[i]
    return max_gap_date, max_gap


def main():
    filename = "./weather(146)_2022-2022.csv"
    weather_data = get_weather_data(filename)


    dates = [[data[0], data[1], data[2]] for data in weather_data]
    tmax = [data[3] for data in weather_data]
    tmin = [data[5] for data in weather_data]


    max_gap_date, max_gap = maximum_temp_gap(dates, tmax, tmin)

    print(f"일교차가 가장 큰 일자는 {max_gap_date[0]}년 {max_gap_date[1]}월 {max_gap_date[2]}일이고,")
    print(f"해당 일자의 일교차는 {max_gap:.1f}도입니다.")


if __name__ == "__main__":
    main()



