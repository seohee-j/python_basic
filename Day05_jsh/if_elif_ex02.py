

print("*** 음식 메뉴를 고르세요. ***")
print("[된장찌개, 제육덮밥, 볶음밥, 카레밥")
food = input("=>")

if food == "된장찌개":
    print(food, "의 가격은 6500원입니다.")
elif food == "제육덮밥":
    print(food, "의 가격은 7000원입니다.")
elif food == "볶음밥":
    print(food, "의 가격은 5500원입니다.")
elif food == "카레밥":
    print(food, "의 가격은 6000원입니다.")
else:
    print(food, "은(는) 존재하지 않는 메뉴입니다.")