def gugudan(dan):
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i)

dan = int(input("출력할 구구단의 단을 입력하세요: "))
gugudan(dan)
