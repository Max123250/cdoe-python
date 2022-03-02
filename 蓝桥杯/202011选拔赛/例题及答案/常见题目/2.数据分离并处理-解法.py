#数据处理类的题目
#输入：n个数据（2<=n<=15，每个数据用','分隔，输出输入了几个数，
#输出：个数，最大数，最小数，由大到小排序，总和、平均值等

a = input(':') # 让用户输入
lst = list(eval(a)) # 这步是核心，分离出n个数，放进列表，
                    # 注意lst是变量名不能数字开头
print(len(lst)) # 输出用户输入数据的个数
print(max(lst)) # 输出最大数
print(min(lst)) # 输出最小数
new = lst[:] # 复制列表 如果是排序后还有其他题就需要先复制出来
             # 如果排序之后没题目就不用复制
new.sort() # 从大到小
print(new)
new.sort(reverse=True) # 从大到小 
print(new)

sums = 0 # 总和变量
for i in range(len(new)):# for循环逐个累加列表中的数
    sums += new[i]
print(sums) # 输出总和
print(sums/5)# 输出平均值

# 字母映射，可以输入测试数列 9,12,15,22,5,21,214
# 输出：ILOVEU[bad]
b = ["A","B","C","D","E","F","G","H","I"
     ,"J","K","L","M","N","O","P","Q"
     ,"R","S","T","U","V","W","X","Y","Z"]
s = ""
for i in range(len(lst)):
    if 1<=lst[i]<=26:
        s+=b[lst[i]-1]   
    else:
        s+="[bad]"
print(s)



    
