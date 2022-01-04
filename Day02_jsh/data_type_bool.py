
'''
* 논리형(boolean)
- 논리형 데이터 타입은 명제가 참일 경우 True, 거짓일 경우 False값을 가진다.
'''

b1 = True
b2 = False

print(type(b1))

# b3 = true  (x)  # 대문자 True는 키워드이고, 소문자 true는 변수.
b4 = "True"       # 문자열 저장.
print(type(b4))  

'''
* 비교 연산자 (==, !=, <. <=, >, >=)
- 좌항과 우항을 비교하여 논리값을 도출하는 연산자이다.
'''

a = 5
print(a < 10)
print(a >= 10)
print(a != 10)

b = a == 5  # =은 연산 순위가 가장 낮음. a == 5가 True이기 때문에 True를 b에 저장.
print(type(b))
# (10 + 3) * 5

'''
- 문자열도 동등, 비동등 비교를 할 수 있다.
- 단, 대/소문자까지 정확히 일치해야 True를 도출한다.
'''

print("-------------")
password = "abc1234"
print(password == "Abc1234")
print(password == "abc1234")

'''
- 문자열도 대/소 비교가 가능하다.
- 문자열끼리 크기를 비교할 때는 사전 순서대로 비교한다.
- 사전에서 앞에 등장하는 단어를 작다고 본다.
'''
print("-------------")
print("apple" < "grape")
print("감자" > "양파")
print("Apple" < "감자")
print("peach" < "Zebra")
