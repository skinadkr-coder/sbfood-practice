# 승빈푸드 대리점 수수료 계산기

grade = "A"          # 여기서 "A" 또는 "B"로 바꿔가며 테스트하세요
order_amount = 100000  # 주문금액 (단위: 원)

if grade == "A":
    fee_rate = 0.05
    print("A등급 대리점: 수수료 5%")
elif grade == "B":
    fee_rate = 0.10
    print("B등급 대리점: 수수료 10%")
else:
    fee_rate = 0
    print("등급을 확인해 주세요.")

fee = order_amount * fee_rate
print(f"주문금액: {order_amount:,}원")
print(f"수수료: {fee:,.0f}원")
