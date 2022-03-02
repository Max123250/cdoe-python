list = []
num1 = int(input())
num2 = int(input())
num3 = int(input())
list.append(num1)
list.append(num2)
list.append(num3)
list.sort()
for i in range(3):
    print(list[i])
