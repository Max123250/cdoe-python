num = int(input())
name = []
if num > 9:
    print("输入不正确")
else:
    name.append(num)
    if num > 6:
        for i in range(7):
            num += 9
            name.append(num)
    else:
        for i in range(8):
            num += 9
            name.append(num)
    print(name)
