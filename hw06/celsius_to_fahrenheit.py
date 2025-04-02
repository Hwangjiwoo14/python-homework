def c2f(t_c):
    return (t_c * 9/5) + 32

t_c = float(input("섭씨 온도를 입력하세요: "))
print("섭씨", t_c, "도는 화씨", c2f(t_c), "도입니다.")

