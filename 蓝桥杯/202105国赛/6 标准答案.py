lst1 = [] # 分离空格的一位数组
lst2 = [] # 包含坐标的二位数组
string = input()
lst1 = string.split(' ')
print(lst1)
for l in lst1:
    ns = list(eval(l))
    #print(ns)
    lst2.append(ns)
print(lst2)

# 存每一个点与其他点的斜率
kss = [] # 二维数组
for i in range(len(lst2)):
    ks = []
    for j in range(len(lst2)):
        if j!=i:
            if lst2[j][0]==lst2[i][0]: # 同一行
                k = -999
            else:
                k = (lst2[j][1]-lst2[i][1])/(lst2[j][0]-lst2[i][0])#算斜率
            ks.append(k)
    kss.append(ks)
print(kss)

count = 0
# 计算相同斜率出现的频次
for i in range(len(kss)):
    cc = 0
    for j in range(len(kss[i])):
        c = kss[i].count(kss[i][j])
        if c > cc:
            cc = c
    if cc > count:
        count = cc
print(count+1) # 要包含自己
