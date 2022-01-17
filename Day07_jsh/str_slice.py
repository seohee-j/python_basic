
'''
* 문자열 슬라이싱
- 문자열 내부의 데이터를 부분적으로 추출할 때 사용하는 방법이다.
ex) 문자열 데이터[begin:end:step]
- range 함수처럼 시작 인덱스는 포함하지만 끝 인덱스는 포함하지 않는다.
'''

s = "python"
print(s[2:5:1]) # tho 추출
print(s[1:4]) # step 생략시 1로 처리
print(s[3:]) # 3번 인덱스부터 끝까지 추출
print(s[:4]) # 처음부터 4번 미만까지 추출

'''
- 문자열을 슬라이싱할 때 [] 내부의 3번째 값으로 step을 지정하면 
   해당 step만큼 건너뛰면서 읽은 후 추출한다.
'''

week = "월화수목금토일"
print(week[::2])
print(week[1:6:2])

print("-"*20)
# 연습퀴즈
# ssn이라는 변수에 주민번호를 입력받아 저장하고
# ex) 220118-2345678
# 문자열 슬라이싱을 통해 주민번호 앞자리와 뒷자리를 따로 출력하시오.


ssn = input("주민등록번호 입력: ")
print("주민등록 앞 번호: ", ssn[:6])
print("주민등록 뒷 번호: ", ssn[7:])
# print(ssn[:2], "년도", ssn[2:4], "월", ssn[4:6], "일 생")
year = ssn[:2]
month = ssn[2:4]
day = ssn[4:6]

if ssn[7] == "1" or ssn[7] == "3":
    gender = "남성"
elif ssn[7] == "2" or ssn[7] == "4":
    gender = "여성"
print(year, "년도", month, "월", day, "일 생")   
    
    
if ssn[7] == "1" or ssn[7] == "2":
    age = 2022 - (1900 + int(year)) + 1
else:
    age = 2022 - (2000 + int(year) + 1)
print(age, "세", gender)




