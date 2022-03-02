'''
for 循环讲解
# 打印1-10
for i in range(1,11):
    print(i)
# 打印1-10所有的奇数
for i in range(1,11,2):
    print(i)
'''

# 回文数问题
a = int(input(':')) # 让用户输入
s = 0
for i in range(1,a+1): # 含头不含尾
    b = str(i)
    c = b[::-1] # 字符串翻转
    if b == c:
        print(b)
        s += 1  # 统计个数
print("*"+str(s))


 
