import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():
    # CSV 읽기 (헤더 포함)
    df = pd.read_csv("merged_weather.csv", header=0)

    # 공백 제거해서 정확한 열 이름 정리
    df.columns = df.columns.str.strip()

    print("열 이름:", df.columns.tolist())
    print("tmax 샘플:", df['tmax'].head())
    print("tmin 샘플:", df['tmin'].head())

    # 숫자형 변환
    df['tmax'] = pd.to_numeric(df['tmax'], errors='coerce')
    df['tmin'] = pd.to_numeric(df['tmin'], errors='coerce')

    # 계절별 필터링
    winter_df = df[df['month'].isin([12, 1, 2])]
    summer_df = df[df['month'].isin([6, 7, 8])]

    # 그래프 그리기
    plt.figure(figsize=(14, 6))

    # 겨울 그래프
    plt.subplot(1, 2, 1)
    plt.hist(winter_df['tmax'].dropna(), bins=30, color='skyblue', label='겨울 최고기온')
    plt.hist(winter_df['tmin'].dropna(), bins=30, color='navy', alpha=0.7, label='겨울 최저기온')
    plt.title('겨울철 온도 분포')
    plt.xlabel('기온(℃)')
    plt.ylabel('빈도')
    plt.legend()

    # 여름 그래프
    plt.subplot(1, 2, 2)
    plt.hist(summer_df['tmax'].dropna(), bins=30, color='orange', label='여름 최고기온')
    plt.hist(summer_df['tmin'].dropna(), bins=30, color='red', alpha=0.7, label='여름 최저기온')
    plt.title('여름철 온도 분포')
    plt.xlabel('기온(℃)')
    plt.ylabel('빈도')
    plt.legend()

    plt.tight_layout()
    plt.savefig("season_temp_histogram.png")
    plt.show()

if __name__ == "__main__":
    main()
