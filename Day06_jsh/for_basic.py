
'''
* 반복문 for
- for 문은 시퀀스 자료형 내의 데이터를 순차적으로 꺼내서 반복 작업하는 반복문이다.
- 시퀀스 자료형은 여러 개의 값들을 모아놓은 집합이며 대표적으로 리스트, 문자열 등이 있다.
- 리스트란 [] 안에 데이터들을 나열해 놓은 일종의 배열이다.

ex) for 제어변수 in 시퀀스 자료형 데이터:
        반복 실행할 코드
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(type(nums))

for stu_num in nums:
    print(stu_num, "번 학생 성적처리 완료!!")
    
print("-"*20)
sum = 0
for n in nums:
    sum += n
print("1~10까지의 누적 합: ", sum)



'''
* 내장함수 range(begin, end, step)
- 순차적으로 증가하는 정수 리스트로 만들 때 대괄호 안에 데이터를
   콤마로 일일이 나열하기보다는 range 함수를 사용하여 쉽게 리스트를 생성할 수 있다.
   
ex) range(시작 값, 끝 값, 증감 값)
- 시작 값은 포함하지만 끝 갚은 포함하지 않는다.
'''
print("-"*30)
a = list(range(1, 11, 1))
print(a)

b = list(range(4, 15))  # 증감 값 생략 시 1로 처리
print(b)

c = list(range(1, 11, 3))
print(c)

# range에 값을 하나만 주면 끝 값으로 처리, 시작값을 0으로 처리
d = list(range(6))  # range(0, 6, 1)
print(d)


# 1~100까지의 누적 합계를 구하는 for문의 사용 예
sum = 0
n = 1   # begin
while n < 101:  # end
    sum += n
    n += 1  # step
print("1~100까지의 누적 합: ", sum)


# for 문으로 바꾸면
sum = 0
for n in range(1, 101, 1):
    sum += n
print("1~100까지의 누적 합: ", sum)


print("-"*30)

# 1 ~ 100까지의 8의 배수 가로로 모두 출력하기
# while 문을
n = 1
while n < 101:
    if n % 8 == 0:
        print(n, end=" ")
    n += 1
print()   

# for 문으로 변경
for n in range(1, 101):
    if n % 8 == 0:
        print(n, end=" ")
print()
    
    
    
print("-"*40)
# 1 ~ 9876사이의 정수 중 13의 배수의 개수를 출력    
# while 문을
n = 1
cnt = 0
while n <= 9876:
    if n % 13 == 0:
        cnt += 1
    n += 1
print("13의 배수 갯수: ", cnt)


# for 문으로 변경
cnt = 0
for n in range(1, 9876):
        if n % 13 == 0:
            cnt += 1
print("13의 배수 갯수: ", cnt)    

'''
# for 문으로 변경하는 연습 quiz
- 정수 x 와 y를 입력받아 x부터 y까지의 누적합을 처리하는 코드를 
   for 문과 range() 를 사용하요 구성하시오.
'''
print("-"*30)

x = int(input("정수x 입력:"))
y = int(input("정수y 입력:"))
sum = 0
for n in range(x, y+1):
    sum += n
print(x, "와 ", y, "의 누적 합계: ", sum)
    





