
'''
* 중첩 if문
- 중첩 if문은 if 블록 내부에 새로운 if문이 있는 형태이다.
- 바깥쪽 if문의 조건을 검사한 후 True가 나올 경우 
   다시 내부의 if문을 검사하는 형태로 조건 판단을 한다. 
'''

height = float(input("키: "))
age = int(input("나이: "))

if height >= 130:
    if age >= 8:
        print("놀이기구 탑승이 가능합니다.")
    else:
        print("나이가 8세 미만입니다.")
        print("놀이기구 탑승이 불가능합니다.")
else:
    print("키가 130cm 미만입니다.")
    print("놀이기구를 탈 수 없습니다.")
    