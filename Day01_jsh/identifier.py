
'''
* 식별자(identifier)
1. 식별자는 사용자 정의로 데이터에 이름을 붙여놓은 것을 말한다.
2. 식별자 이름은 중복하여 사용할 수 없다.
3. 식별자의 이름은 숫자로 시작하면 안 된다.
4. 식별자 이름에 공백을 포함할 수 없다.
5. 대/소문자를 다르게 쓰면 다른 식별자로 인식한다.
6. if, while과 같은 이미 기능이 지정되어 있는 키워드(예약어)는 식별자 이름으로 사용할 수 없다.
7. print()와 같은 내장함수의 이름도 식별자 이름으로 사용할 수는 있지만,
    해당 함수의 이름을 변수로 지정할 경우 더 이상 함수의 기능을 사용할 수 없다.
'''

name1 = "Emily"
name2 = "Jane"
print(name1)
print(name2)

num7ber = 7    # (O)
# 7number = 7  # (X)

# user birth day = 211214 (X)
userbirthday = 211214   # 가능하지만 아래 방법으로 사용하는 것을 선호
user_birth_day = 211214
UserBirthDay = 211214

banana = "바나나"
Banana = "바나나"
BaNaNa = "뻐네이너"
print(banana)
print(Banana)
print(BaNaNa)

# if = "만약에" (X)
If = "만약에"

# print = "안녕"    # 변수로 지정할 경우 print()를 아래에서 더이상 사용할 수 없음
print("안녕하세요")

東方神起 = "동방신기"
print(東方神起)
야옹이 = "cat"
print(야옹이)







