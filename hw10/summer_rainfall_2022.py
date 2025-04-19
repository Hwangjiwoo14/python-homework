import csv


def read_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i >= 10:
                break
            print(row)


def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")

            tokens = [token.strip() for token in tokens]
            try:

                weather_datas.append(float(tokens[col_idx]))
            except ValueError:
                pass
    return weather_datas

def get_weather_data_int(fname, col_idx):
    data = []
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            tokens = [token.strip() for token in tokens]
            try:

                data.append(int(tokens[col_idx]))
            except ValueError:
                pass
    return data



def sumifs(rainfalls, months, selected=[6, 7, 8]):
    total = 0
    for i in range(len(rainfalls)):
        if months[i] in selected:
            total += rainfalls[i]
    return total


def main():
    filename = r"C:\code\ppp2025\hw10\weather(146)_2022-2022.csv"

    rainfalls = get_weather_data(filename, 9)
    months = get_weather_data_int(filename, 1)

    print(f"rainfalls (첫 10개): {rainfalls[:10]}")
    print(f"months (첫 10개): {months[:10]}")
    summer_rainfall = sumifs(rainfalls, months, selected=[6, 7, 8])
    print(f"2022년 여름철(6~8월) 총 강수량은 {summer_rainfall:.1f}mm입니다.")


if __name__ == "__main__":
    main()
