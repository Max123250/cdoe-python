
#题目：输入n,输出1到n之间的所有数的平方,输出一行排列

m = 1 # 求1到n，那么m就为固定的数1
n = int(input())
lst = []
for i in range(m,n+1): # 包含n
    a = i*i
    lst.append(str(a))
print(",".join(lst))# 逐行打印输出





