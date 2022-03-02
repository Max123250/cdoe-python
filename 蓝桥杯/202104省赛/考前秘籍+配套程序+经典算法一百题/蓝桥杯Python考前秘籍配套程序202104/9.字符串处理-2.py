

a = input()
b = input()
'''
a = "to"
b = "to be or not to be is a question."
'''

# 如果遇到不区分大小，一般转化成大写
a = a.upper()
b = b.upper()

r = 0     # 找到目标的位置
pos = 0   # 位置
count = 0 # 记录总个数
lst = []  # 记录所有位置
#first = True #是否为第一次 
#firstPos = -1 # 第一次的位置
while r >=0:
    r = b.find(a,pos)
    if r >= 0:
        count += 1
        lst.append(r) 
        '''
        if first:
            firstPos = r # 记录第一次的位置
            first = False
        '''
    pos = r + len(a)

print(lst)

# 判断是否为独立的单词
# 复制列表
lst_result = lst[:]
for i in range(len(lst)):
    print(i)
    p = lst[i]
    if p == 0:# 在第一个位置
        if b[p+len(a)] != " ":
            lst_result.pop(i)
    elif p+len(a) == len(b): # 在最后一个位置
        if b[p-1] != " ":
            lst_result.pop(i) 
    else:
        # 前后为空格即为独立单词
        if b[p-1] != " " or b[p+len(a)+1] != " ": 
            lst_result.pop(i)

print(len(lst_result), lst_result[0])
    

