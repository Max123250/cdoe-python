#第四题：输入n1与n2,输出他们两个的最大公约数与最小公倍数
n1 = int(input())
n2 = int(input())
bigger = 0
smaller = 0
lnum = 0
hnum = 0
if n1 > n2:
    bigger = n1
else:
    bigger = n2

while True:
    if bigger % n1 == 0 and bigger % n2 == 0:
        lnum = bigger
        break
    bigger += 1

if n1 > n2:
    smaller = n2
else:
    smaller = n1

for i in range(1,smaller + 1):
    if n1 % i == 0 and n2 % i == 0:
        hnum = i
print(str(lnum) + "," + str(hnum))
#未作出（赛后修改做出）