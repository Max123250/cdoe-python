list = list(eval(input()))
list.sort()
p_min = list[0] + list[1]
can = False
if p_min > list[2]:
    print("能组成三角形")
    can = True
else:
    print("不能组成三角形")
    can = False
if can:
    if list[0] == list[1]:
        print("是等腰三角形")
    elif list[0]**2 + list[1]**2 == list[2]**2:
        print("是直角三角形")
    else:
        print("是普通三角形")
