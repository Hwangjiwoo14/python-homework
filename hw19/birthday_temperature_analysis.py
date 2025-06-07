import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():

    df = pd.read_csv("merged_weather.csv", header=0)
    df.columns = df.columns.str.strip()


    df['tmax'] = pd.to_numeric(df['tmax'], errors='coerce')
    df['tmin'] = pd.to_numeric(df['tmin'], errors='coerce')


    birthday_df = df[(df['month'] == 2) & (df['day'] == 4)].copy()
    birthday_df = birthday_df.sort_values(by='year')


    plt.figure(figsize=(12, 6))
    plt.plot(birthday_df['year'], birthday_df['tmax'], marker='o', color='red', label='최고기온')
    plt.plot(birthday_df['year'], birthday_df['tmin'], marker='o', color='blue', label='최저기온')


    max_temp_year = birthday_df.loc[birthday_df['tmax'].idxmax(), 'year']
    min_temp_year = birthday_df.loc[birthday_df['tmin'].idxmin(), 'year']
    plt.axvline(x=max_temp_year, linestyle='--', color='orange', label=f'가장 더운 생일({int(max_temp_year)}년)')
    plt.axvline(x=min_temp_year, linestyle='--', color='navy', label=f'가장 추운 생일({int(min_temp_year)}년)')

    plt.title("2월 4일 생일 기온 변화 (1980~2024)")
    plt.xlabel("연도")
    plt.ylabel("기온(℃)")
    plt.legend()
    plt.grid(True)
    plt.savefig("birthday_temp_feb4.png")
    plt.show()


    before_2005 = birthday_df[birthday_df['year'] < 2005]
    after_2005 = birthday_df[birthday_df['year'] >= 2005]

    plt.figure(figsize=(12, 6))
    plt.plot(before_2005['year'], before_2005['tmax'], color='red', label='2005년 이전 최고기온')
    plt.plot(after_2005['year'], after_2005['tmax'], color='darkred', linestyle='--', label='2005년 이후 최고기온')
    plt.plot(before_2005['year'], before_2005['tmin'], color='blue', label='2005년 이전 최저기온')
    plt.plot(after_2005['year'], after_2005['tmin'], color='navy', linestyle='--', label='2005년 이후 최저기온')

    plt.title("2월 4일 생일 기온 비교 (2005년 기준)")
    plt.xlabel("연도")
    plt.ylabel("기온(℃)")
    plt.legend()
    plt.grid(True)
    plt.savefig("birthday_temp_compare.png")
    plt.show()

if __name__ == "__main__":
    main()
