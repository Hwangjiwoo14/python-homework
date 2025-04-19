def get_weather_data(filename, col_idx):
    datas = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                value = tokens[col_idx].strip()
                datas.append(float(value))
            except:
                datas.append(None) 
    return datas

def get_date_data(filename):
    dates = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            dates.append(tokens[1].strip())
    return dates

def top_3_hottest_days(filename):
    tmax = get_weather_data(filename, 5)
    dates = get_date_data(filename)

    temp_date = []
    for i in range(len(tmax)):
        if tmax[i] is not None:
            temp_date.append((tmax[i], dates[i]))

    temp_date.sort(reverse=True)

    print("가장 더운 날 Top 3")
    for i in range(3):
        print(f"{i+1}. {temp_date[i][1]} - {temp_date[i][0]}℃")

def main():
    filename = "weather(146)_2022-2022.csv"
    top_3_hottest_days(filename)

if __name__ == "__main__":
    main()
