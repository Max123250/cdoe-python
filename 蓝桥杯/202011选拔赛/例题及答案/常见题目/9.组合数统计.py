#题目：用1/3/5/8这4个数字，能组成的互不相同且无重复数字的三位数有哪些？
#共有多少？这些数的和为多少？
'''
【输入】
  无
【输出】
多行数字，每行一个三位数
组成的三位数的总个数
这些三位数的总和
'''
n = 0 # 统计满足条件的数的个数
s = 0 # 用于累计求和的变量
lst = []
for i in [2,4,6,8]: # i为百位数字
    for j in [2,4,6,8]: # j为十位数字
        for k in [2,4,6,8]: # k为个位数字
            if i != j and i != k and j != k:#条件为ijk互不相等，即三位数不重复
                a = 100*i+10*j+k # 此运算得到一个满足条件的数
                lst.append(a)
                s = s + a # 因为要求和，这里做累加
                print(a) # 逐个打印满足条件的数
                n = n+1 
print('共有'+str(n)+'个')
print(f'总和{s}')

# 附加题：要求罗列被3整除的所有数
for i in range(len(lst)):
    if lst[i] % 3 == 0:
        print(lst[i]) # 逐个打印
        

