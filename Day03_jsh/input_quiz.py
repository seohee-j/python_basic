'''
quiz:
1. 회원의 이름과 성별 그리고 나이를 입력받으세요.
2. 이름 변수는 name, 성별은 gender, 나이는 age입니다.
3. 입력받은 값을 통해 회원의 이름, 성별, 나이 그리고 출생년도를 출력하세요.
'''
name = input("이름 입력: ")
gender = input("성별 입력 [여성, 남성]: ")
age = int(input("나이 입력: "))
print("이름은 ", name, "이고 성별은 ", gender, "이며 나이는 ", age, "세, "
        , 2022 + 1 - age, "년생 입니다.", sep="")