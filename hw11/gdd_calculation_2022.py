def get_weather_data(fname):
    dates = []
    tavg = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
            tavg.append(float(tokens[4]))
    return dates, tavg

def gdd(tavg, dates):
    temp_sum = 0
    base_temp = 5
    for i in range(len(tavg)):
        if dates[i][1] in [5, 6, 7, 8, 9]:
            if tavg[i] >= base_temp:
                temp_sum = temp_sum + (tavg[i] - base_temp)
    return temp_sum

def main():
    filename = "./weather(146)_2022-2022.csv"

    dates, tavg = get_weather_data(filename)

    total_gdd = gdd(tavg, dates)

    print(f"2022년 5월~9월 생육도일(GDD)은 {total_gdd:.1f}도입니다.")

if __name__ == "__main__":
    main()
