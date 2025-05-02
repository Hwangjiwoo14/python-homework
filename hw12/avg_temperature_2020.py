import csv

def average(nums):
    return sum(nums) / len(nums)

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:  # 첫 줄은 헤더
            tokens = line.strip().split(",")
            if len(tokens) > col_idx:
                value = tokens[col_idx]
                if value:
                    try:
                        weather_datas.append(float(value))
                    except ValueError:
                        continue
    return weather_datas



def main():
    filename = "weather(146)_2020-2020.csv"
    col_idx = 4
    tavgs = get_weather_data(filename, col_idx)

    if len(tavgs) > 0:
        avg_temp = average(tavgs)
        with open("result_avg_temp_2020.txt", "w", encoding="utf-8") as fout:
            fout.write(f"2020년 연평균 기온: {avg_temp:.2f}°C\n")
    else:
        print("데이터가 없습니다.")

if __name__ == "__main__":
    main()
