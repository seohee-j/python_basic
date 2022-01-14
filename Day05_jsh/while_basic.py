
'''
* 반복문 (Loop)
- 반복문은 유사한 명령을 반복해서 실행하는 제어문이다.
- 파이썬의 반복문 키워드는 while, for가 있다.

* while
제어변수 선언 (begin)
while 논리형 조건식 (end):
    반복 실행할 코드
    제어변수의 증감식 (step)
    
- 제어변수란 반복문의 반복 횟수를 제어할 변수다.
'''

stu_num = 1
while stu_num <= 10:                   # 논리형 조건식
    print(stu_num, "번 성적처리 완료!")     # 반복 실행할 코드
    stu_num += 1                       # 제어변수의 증감식
    
print(stu_num)  # 11