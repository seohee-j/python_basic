
# 1 ~ 10까지의 누적 합계를 구하는 로직
sum = 0
n = 1   # 제어변수 (begin)
while n < 11:   # 조건식 (end)
    sum += n 
    n += 1  # 증감식 (step)

print("1~10까지의 누적 합: ", sum)


# 7 ~ 100까지의 7의 배수 가로로 모두 출력하기

n = 7
while n < 101:
    print(n, end=" ")
    n += 7
    
print()     # 줄개행만 하라는 명령

# 1 ~ 100까지의 8의 배수 가로로 모두 출력하기
n = 1
while n < 101:
    if n % 8 == 0:
        print(n, end=" ")
    n += 1
print()    


# 1 ~ 9876사이의 정수 중 13의 배수의 개수를 출력
print("-"*40)

n = 0
cnt = 0
while n <= 9876:
    if n % 13 == 0:
        cnt += 1
    n += 1
print("13의 배수 갯수: ", cnt)






