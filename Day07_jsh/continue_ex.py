
'''
* continue
- break가 반복문을 강제로 종료시킨다면,
  continue는 반복 1회만 건너뛰고 다음 반복부터는 정상적으로 실행하는 탈출문이다.
'''

points = [89, 92, 71, 68, -1, 87, -1, 100]

for p in points:
    if p == -1:
        continue
    print(p, end=" ")
print("\n점수 처리 완료!")


# 출력: 1,3,5,7,9
for a in range(1, 11):
    # 종속 코드가 단 한 줄이라면 줄개행을 하지 않아도 된다.
    if a % 2 == 0: continue
    print(a, end=" ")
print("\n반복문 종료!")