
'''
* 문자열 인덱싱
- 파이썬은 문장을 기본 타입으로 지원할 뿐만 아니라 문자열을 관리하는 풍부한 명령을 가지고 있다.
- 문자열은 메모리상에 개별 문자들이 일렬로 늘어선 형태로 저장된다.
- 문자열의 각 문자들은 인덱스(index)로 관리되며 맨 앞 글자부터 0번이 부여되고, 
   그 뒤부터 1씩 증가하는 순차적인 번호가 부여된다.
'''

s = "python"
print(s[2])
print(s[3])
print(s[-5])
print(s[1] == s[-5])

# 인덱싱을 할 때 문자열의 인덱스 법위를 벗어나는 참조는 에러를 발생시킴.
# print(s[6])

for c in s:
    print(c, end="!")
print()

for day in "월화수목금토일":
    print(day + "요일")
    
    
    
ssn = "941211-4234567"

if ssn[7] == "2" or ssn[7] == "4":
    print("여성입니다.")
elif ssn[7] == "1" or ssn[7] == "3":
    print("남성입니다.")


