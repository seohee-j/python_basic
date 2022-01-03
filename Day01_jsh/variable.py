
'''
* 변수(variable)
1. 변수는 데이터를 저장하기 위한 공간에 이름을 붙여둔 것이다.
2. 하나의 변수에는 하나의 데이터만 저장할 수 있다.
3. 변수의 값은 실행 중에 언제든지 변경할 수 있다.
'''

print("실행 테스트!")
a = 10 + 9
print(a)

a = 100
print(a)

print("-----------")

n1 = 15
n2 = 3
result = n1 * n2
print(result)

n2 = 5
print(result)   #45
result = n1 * n2    # 이 코드를 다시 적어주지 않는다면 위의 result 값인 45가 출력됨.
print(result)   #75

apple = "사과"    # 따옴표가 없다면 변수가 된다. 위에 사과라는 변수가 없기 때문에 에러.
print(apple)


