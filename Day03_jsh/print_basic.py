
'''
* 표준 출력 함수 print()
- 파이썬의 표준 출력 함수는 print이고 괄호 안에 출력하고 싶은 
   변수, 상수, 수식 등을 적으면 콘솔 창에 텍스트 출력을 실행한다.
'''

value = 1234
name = "신사임당"

print(value)
print(name)
print(9876)
print("홍길동")
print(value * 3)

'''
- 출력할 데이터가 ㅇ러 개라면 괄호 안에 출력할 데이터들을 콤마(,)로 나열하여 작성한다.
- 이때 여러 개의 값들을 공백과 함께 가로로 나란히 출력한다.
'''

dog = "멍멍이"
cat = "야옹이"
print(dog, cat, 28)

'''
- print 함수 내부에는 sep이라는 속성이 존재한다.
- sep은 separator의 약자로 구분자라고 불린다.
- sep의 값은 디폴트로 " " 공백 문자열이 지정되어 있다.
'''
print("-" * 20)
print(dog, cat, 28, sep=" ")
print(dog, cat, 28, sep=",")
print(dog, cat, 28, sep=" =>")
print(dog, cat, 28, sep="")

print("-" * 20)
f1 = "닭강정"
f2 = "떡볶이"
f3 = "마라탕"
f4 = "삼겹살"

# Quiz
# : sep 속성을 사용하여 '닭강정 먹고 김말이 먹고 볶음밥 먹고 짜장면'을 
# 하나의 print로 출력하시오.

print(f1, f2, f3, f4, sep=" 먹고 " )

'''
- 파이썬의 print 함수가 자동으로 줄 개행을 하는 이유는 
  함수 내부에 end라는 속성값이 지정되어 있으며 디폴트로 "\n"이 정해져 있기 때문이다.
'''

print("-" * 20)
print(dog, end="\n")
print(cat, end="\n")

print(dog, end="랑 ")
print(cat, sep=" ", end="\n")
print("안녕", "잘가", end="\n", sep=" ")
# print(end="\n", sep=" ", dog, "헬로") # (X) 출력할 데이터가 end와 sep보다 앞에 있어야 한다.


