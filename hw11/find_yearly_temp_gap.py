def get_weather_data(fname):
    dates = []
    tmax = []
    tmin = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            tx = float(tokens[3])
            tm = float(tokens[5])

            dates.append([year, month, day])
            tmax.append(tx)
            tmin.append(tm)
    return dates, tmax, tmin


def maximum_temp_gap_by_year(dates, tmax, tmin):
    results = {}

    for i in range(len(dates)):
        year = dates[i][0]
        gap = tmax[i] - tmin[i]

        if year not in results:
            results[year] = (dates[i], gap)
        else:
            if gap > results[year][1]:
                results[year] = (dates[i], gap)

    return results


def main():
    filename = "./weather(146)_2001-2022.csv"
    dates, tmax, tmin = get_weather_data(filename)
    year_max_gaps = maximum_temp_gap_by_year(dates, tmax, tmin)

    for year in sorted(year_max_gaps.keys()):
        date, gap = year_max_gaps[year]
        print(f"{date[0]}/{date[1]:02d}/{date[2]:02d} {gap:.1f}")


if __name__ == "__main__":
    main()
