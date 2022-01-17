
'''
* 탈출문(흐름 제어문) - break, continue
- 반복문은 조건을 만족하는 동안 계속 코드를 반복하기 때문에
   한 번 반복이 시작되면 반복 횟수가 끝날 때까지 반복을 진행한다.
- 하지만 중간에 어떤 이유로 반복을 중지하거나 현재 반복을 건너뛰어야 할 경우 탈출문을 사용한다.

* break
- break는 현재 반복문을 즉시 종료시키고 반복문 블록을 탈출한다.
- 일반적으로 특정 조건하에서 반복문을 종료시키므로 if문과 함께 사용한다.
'''

for a in range(1, 11):
    if a == 6:
        break
    print(a, end=" ")
print("\n반복문 종료!")

points = [92, 64, -74, 158, 98]

for p in points:
    if (p > 100) or (p < 0):
        print("\n점수 처리 과정에서 문제 발생! 성적을 확인하세요.")
        break
    print(p, end=" ")
print("\n점수 처리 완료!")