
'''
* 논리 연산자(&, |, and, or, not)
- 논리값의 연산을 수행하는 연산자이다.
* &, and 연산자는 좌항과 우항의 조건식의 결과가 모두 True 일 경우에만 전체 결과를 True로 도출한다.
'''

a = 33

if (a > 1) & (a < 10):
    print("a는 1보다 크고 10보다 작다.")
print("test!!")

# 파이썬은 위의 식을 연결해서 표현할 수 있다.
if 1 < a < 10:
    print("OK!!")
    
# |, or 연산자는 좌항과 우항의 조건식의 결과가 하나만 True여도 전체결과를 True로 도출한다.
b = 5

if (b == 2) | (b == 5):
    print("b는 2또는 5이다.")
    
'''
* 단축 평가(short circuit) - and, or
- 논리 연산 수행 시 좌항에서 전체 결과가 판명날 경우
   우항 연산을 진행하지 않는 연산자이다.
'''

c = 2

if (c == 0) | (10 / c == 5):
    print("에러 없이 통과함!")
    
# not 연산자는 논리값을 반전시킨다. (T -> F, F -> T)
d = 10

if not d < 0:
    print("d는 0보다 작지 않습니다.")
    
    
print("-"*20)

'''
- C언어에서는 정수 0을 False로 해석하고, 
   0이 아닌 모든 정수를 True로 해석한다.
- 파이썬에서도 C의 논리 해석을 그대로 사용할 수 있다.
'''


drink = 2

if not drink:
    print("음료수가 모두 품절되었습니다.")
else:
    print("음료수가 ", drink, "개 남았습니다.")   
    
    
    
    
    
    
    
    
    
    