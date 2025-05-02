import os
import requests

def download_weather_data_2020(filename):
    if not os.path.exists(filename):
        url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8-sig") as f:
            f.write(resp.text)


def get_weather_data(filename, col_idx):
    data = []
    with open(filename, encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            try:
                value = float(tokens[col_idx])
                data.append(value)
            except:
                continue
    return data

def main():
    filename = "weather_146_2020.csv"
    download_weather_data_2020(filename)

    rainfalls = get_weather_data(filename, 9)

    total_rainfall = sum(rainfalls)

   
    with open("result_3_total_rainfall.txt", "w") as f:
        f.write("2020년 총 강수량: {:.1f} mm\n".format(total_rainfall))

if __name__ == "__main__":
    main()
