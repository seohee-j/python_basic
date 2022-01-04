
# 문자열과 정수의 상호변환
name = "홍길동"
score = 90
# score = "90"  # 연산을 할 수 없게 됨.

# print(name + "의 점수는: " + score) # 타입이 일치하지 않는 데이터를 더할 수 없음.

'''
- 문자열과 정수의 + 연산 진행시 타입이 일치하지 않는다면 에러 발생.
   따라서 타입을 어느 한쪽으로 맞춰야 한다.
   
- 정수를 문자열로 변환할 때는 str()함수를 사용한다.
'''
print(name + "의 점수는: " + str(score))
score = str(score)
print(type(score))  #str

n1 = 10
n2 = "32"
# print(n1 + n2)  # 타입 불일치
print(str(n1) + n2)

# 문자열을 정수로 변환할 때는 int()함수를 사용한다.
print(n1 + int(n2))
print(n1 + int("20"))
# print(n1 + int("20%")) (X)
# print(n1 + int("3.14")) (X)


