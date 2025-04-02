mart_price = { "우유": 2800, "계란": 300,"빵": 1200, "물":1700}
cart = ["우유", "빵", "빵", "빵", "계란"]
#cart = []
#cart.append("우유")
#cart.append("빵")

total_cost = 0
for item in cart:
    total_cost += mart_price[item]
print("총 구매금액은 {:,}원입니다.".format(total_cost) )