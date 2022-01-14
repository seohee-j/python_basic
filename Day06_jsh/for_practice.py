
'''
# 구구단 단수를 입력받아 입력 받은 단수의 구구단이 출력되게 하세요.
'''

dan = int(input("구구단 단 수: " ))
print("*** 구구단", dan, "단 ***")
for hang in range(1, 10, 1):
    print(dan, "x", hang, "=", dan*hang)

