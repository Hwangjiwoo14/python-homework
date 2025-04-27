def get_weather_data(fname):
    dates = []
    tavg = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            ta = float(tokens[4])

            dates.append([year, month, day])
            tavg.append(ta)
    return dates, tavg


def calculate_gdd_by_year(dates, tavg):
    results = {}
    base_temp = 5.0

    for i in range(len(dates)):
        year, month, day = dates[i]
        temp = tavg[i]

        if 5 <= month <= 9:
            if year not in results:
                results[year] = 0.0

            if temp >= base_temp:
                results[year] += (temp - base_temp)

    return results


def main():
    filename = "./weather(146)_2001-2022.csv"
    dates, tavg = get_weather_data(filename)
    gdd_by_year = calculate_gdd_by_year(dates, tavg)

    for year in sorted(gdd_by_year.keys()):
        print(f"{year} {gdd_by_year[year]:.1f}")


if __name__ == "__main__":
    main()
