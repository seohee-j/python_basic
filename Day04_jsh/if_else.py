
'''
* if ~ else
- if 블록의 조건식 결과가 True 일 경우에만 실행된다면
   else 블록은 위의 if의 조건식의 결과에 따라 값이 False 일 경우에만 실행된다.  
- if 뒤에는 반드시 논리값을 반환하는 조건식을 적어야 하지만 
   else 뒤에는 아무것도 적지 않는다.
- if는 단독 사용이 가능하지만 else는 반드시 if와 함께 사용해야 한다.
'''

money = int(input("얼마 있니??"))
if money >= 20000:
    print(("치킨 시켜먹자!!"))
    print(("신나는 치킨파티야~ >_<"))
else:
    print("그냥 라면이나 먹어야겠네 ㅠㅠ")
print("야식은 적당히~~")