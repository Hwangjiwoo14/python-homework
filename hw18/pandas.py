import requests
import pandas as pd
import os
import tkinter as tk
from tkinter import simpledialog
from sfarm_hw import submit_to_api

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력", prompt=text)

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def load_or_download(station_id, year, filename):
    if not os.path.exists(filename):
        download_weather(station_id, year, filename)
    return pd.read_csv(filename, skipinitialspace=True)

def calculate_max_temp_gap(df):
    return (df['tmax'] - df['tmin']).max()

def main():
    df_2015 = load_or_download(146, 2015, "weather_146_2015.csv")
    df_2022 = load_or_download(146, 2022, "weather_146_2022.csv")
    df_2024_146 = load_or_download(146, 2024, "weather_146_2024.csv")
    df_2024_119 = load_or_download(119, 2024, "weather_119_2024.csv")

    answer1 = round(df_2015['rainfall'].sum(), 1)
    answer2 = df_2022['tavg'].max()
    answer3 = round(calculate_max_temp_gap(df_2024_146), 1)
    answer4 = round(abs(df_2024_146['rainfall'].sum() - df_2024_119['rainfall'].sum()), 1)


    window = tk.Tk()
    window.withdraw()
    name = gui_input("이름을 입력하세요:")
    affiliation = gui_input("학과를 입력하세요:")
    student_id = gui_input("학번을 입력하세요:")


    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()
