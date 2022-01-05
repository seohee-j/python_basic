
'''
- 처음부터 입력한 값을 정수나 실수 형태로 사용할 것으로 판단된다면
  입력받을 때부터 정수나 실수 형태로 입력받을 수 있다.
'''
price = int(input("가격: "))
sale_rate = float(input("할인율:"))

print("price의 타입: ", type(price))
print("sale_rate의 타입: ", type(sale_rate))

