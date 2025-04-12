import csv

file_path = "weather_data.csv"

total_temp = 0
day_count = 0
rainy_days = 0
total_rainfall = 0

with open(file_path, mode="r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        tavg = float(row["tavg"])
        rainfall = float(row["rainfall"])

        total_temp += tavg
        total_rainfall += rainfall
        day_count += 1

        if rainfall >= 5:
            rainy_days += 1

average_temp = total_temp / day_count if day_count else 0

print(f"연평균 기온: {average_temp:.2f}℃")
print(f"5mm 이상 강우일수: {rainy_days}일")
print(f"총 강우량: {total_rainfall:.1f}mm")
