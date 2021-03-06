
'''
* 문자열 연산
- 파이썬은 문자열의 덧셈 연산과 곱셈 연산을 지원한다.
- 문자열의 덧셈 연산시 문자열을 서로 결합한다.
'''

s1 = "오늘 저녁은 "
s2 = "치킨과 피자입니다."
print(s1 + s2 + "꼭 먹어야지!!><")

'''
- 파이썬에서는 문자열의 곱셈 연산을 지원하고 있다.
- 곱셈 연산자(*)로 문자열을 정해진 수만큼 반복할 수 있다.
- 이때 반드시 좌항에는 문자열이, 우항에는 정수가 와야 한다.
- 문자열끼리 곱하거나 문자열과 실수를 곱할 수는 없다.
'''
print(s1 * 2)
print("배고파" * 3)
print("-" * 17)
# print(s1 * s2)  (X)