num = int(input())
for j in range(num):
    for i in range(num,0,-1):
        print(i,end = " ")
    num -= 1
    print()
