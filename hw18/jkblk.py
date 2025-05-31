import requests
import pandas as pd

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)


def main():
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    print(df.head())
    print(df["rainfall"].sum())



if __name__ == "__main__":
    main()