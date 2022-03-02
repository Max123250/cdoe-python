thing = input()
num = int(input())
for i in range(1,num + 2,2):
    meny = i
    space = int((num - meny) / 2)
    print("{}{}".format(" " * space,thing * meny))

for i in range(num - 2,0,-2):
    meny = i
    space = int((num - meny) / 2)
    print("{}{}".format(" " * space,thing * meny))
