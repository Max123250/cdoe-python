
# 题目：输入n1,n2,输出他们的最大公约数和最小公倍数

n1 = int(input())
n2 = int(input())

m = 0
if n1>n2:
    m = n2
else:
    m = n2

# 最大公约数    
gys = 1 # 公约数
for i in range(1, m):# 完整循环，因为要找最大
    if n1 % i == 0 and n2 % i == 0:
        gys = i 
print(gys)


# 最小公倍数
if n1>n2:
    m = n1
else:
    m = n2
gbs = m # 公倍数
for i in range(m, n1*n2+1):
    if i % n1 == 0 and i % n2 == 0:
        gbs = i
        break # 找到即可退出，因为要找最小
print(gbs)


