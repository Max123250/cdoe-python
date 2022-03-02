num1 = int(input())
num2 = int(input())
list = []
for i in range(num1,num2 + 1):
    if i % 7 == 0:
        if not i % 5 == 0:
            list.append(str(i))
print(",".join(list))