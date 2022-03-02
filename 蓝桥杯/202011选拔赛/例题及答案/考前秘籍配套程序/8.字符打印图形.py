a = input() # 填充的字符
n = int(input()) # 最长个数
for i in range(1,n,2):# 1颗星到n-2颗星
    # 字符乘以数量等于输出多个字符
    print(' '*((n-i)//2), end='') # 先打印空格
    print(a*i) # 输出i个a字符
for i in range(n,-1,-2):# 不含尾所以写-1
    print(' '*((n-i)//2), end='') # 先打印空格
    print(a*i) # 输出i个a字符





        
