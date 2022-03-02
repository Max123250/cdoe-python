num = int(input())
if num % 2 == 0:
    num -= 1
for i in range(1,num,2):
    num += i
print(num)
