
'''
* 중첩 반복문
- 반복문 안에는 또 다른 반복문이 들어가서 중첩 형태의 반복문을 구성하는 것이 가능하다.
- 반복 상황 내에서 또 다른 반복문을 실행하는 구조이다.
- 중첩 루프 작성 시 주의점은 들여 쓰기에 주의하여 해당 실행 코드가 어떤 반복문의 실행문인지 잘 구분해야 한다.
'''


''' for문 구구단
for dan in range(2, 10):
    print("구구단", dan, "단")
    print("="*20)
    
    for hang in range(1, 10):
        print(dan, "x", hang, "=", dan * hang)
    print("-"*20)
'''

# while문 구구단으로 변경

dan = 2
while dan < 10:
    print("구구단", dan, "단")
    print("="*20)
    hang = 1
    while hang < 10:
        print(dan, "x", hang, "=", dan * hang)
        hang += 1
    print("-"*20)
    dan += 1


# 삼각형 별 피라미드 그리기
'''
*
**
***
****
*****
'''

print("^"*20)

for x in range(1,6):
    for y in range(x):
        print("*", end="")
    print()

'''
*****
****
***
**
*
'''

print("^"*20)

for x in range(1,6):
    for y in range(0, 6-x):
        print("*", end="")
    print()

'''
    *
   **
  ***
 ****
*****
'''

print("^"*20)

for x in range(1,6):
    for y1 in range(5-x):
        print(" ", end="")
    for y2 in range(x):
        print("*", end="")
    print()
    
    
'''
*****
 ****
  ***
   **
    *
'''
print("^"*20)
for x in range(1,6):
    for y1 in range(x-1):
        print(" ", end="")
    for y2 in range(6-x):
        print("*", end="")
    print()
 
'''
    *
   ***
  *****
 *******
*********
'''   
print("^"*20)
for x in range(1,6):
    for y1 in range(5-x):
        print(" ", end="")
    for y2 in range(x*2-1):
        print("*", end="")
    print()

    
    
    