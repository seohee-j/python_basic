
'''
- input 함수로 입력받은 데이터는 무조건 문자열로 처리되기 때문에 
  값을 숫자로 입력해도 수치 연산이 실행되지 않는다.
'''

n1 = input("1번째 정수: ")
n2 = input("2번째 정수: ")

# print("두 수의 덧셈 결과: ", n1 + n2)

print("두 수의 덧셈 결과: ", int(n1) + int(n2))
print("두 수의 뺄셈 결과: ", int(n1) - int(n2))
print("두 수의 곱셈 결과: ", int(n1) * int(n2))
print("두 수의 니눗셈 결과: ", int(n1) / int(n2))