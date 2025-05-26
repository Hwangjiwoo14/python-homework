import requests
import os
from sfarm_hw import submit_to_api

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
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

def maximum_temp_gap(tmax, tmin):
    max_gap = 0
    for i in range(1, 365):
        gap = tmax[i] - tmin[i]
        if gap > max_gap:
            max_gap = gap
    return  max_gap


def main():
    filename1 = "./weather_146_2015.csv"
    if not os.path.exists(filename1):
        download_weather(146, 2015, filename1)

    filename2 = "./weather_146_2022.csv"
    if not os.path.exists(filename2):
        download_weather(146, 2022, filename2)

    filename3 = "./weather_146_2024.csv"
    if not os.path.exists(filename3):
        download_weather(146, 2024, filename3)

    filename4 = "./weather_119_2024.csv"
    if not os.path.exists(filename4):
        download_weather(119, 2024, filename4)
    # dates = get_weather_date(filename)

    rainfall2015 = get_weather_data(filename1, 9)
    tavg2022 = get_weather_data(filename2, 4)
    tmin2024 = get_weather_data(filename3, 5)
    tmax2024 = get_weather_data(filename3, 3)
    rainfall2024 = get_weather_data(filename3, 9)
    rainfall2024_2 = get_weather_data(filename4, 9)


    print(round(sum(rainfall2015), 1))
    print(max(tavg2022))
    print(maximum_temp_gap(tmax2024, tmin2024))
    print(round(abs(sum(rainfall2024)-sum(rainfall2024_2))), 1)

    rainfall_gap = abs(sum(rainfall2024)-sum(rainfall2024_2))



    name = "황지우"
    affiliation = "스마트팜학과"
    student_id = "202410125"

    answer1 = round(sum(rainfall2015), 1)
    answer2 = max(tavg2022)
    answer3 = maximum_temp_gap(tmax2024, tmin2024)
    answer4 = round(rainfall_gap, 1)

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()