# 万能结构，肯定会出这样的程序结构
# 在m和n中找符合规律的数
# 题目1，输入m和n，输出两者之间的被7整除不被5整除的数。
m = int(input()) # 记住input()括号内不要填东西
n = int(input())
lst = []
for i in range(m,n+1): # 包含n
    if i%7==0 and i%5!=0: # 被7整除，且不是5的倍数
        lst.append(str(i)) # 记得把数字转成字符串再存入列表
print(",".join(lst)) # 一行输出

# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# 如果题目要求一行输出一个数，就直接print，不需要用join

# 题目2，输入n，输出1到n之间的偶数，以及个数、总和
m = 1 # 求1到n，那么m就为固定的数1
n = int(input())
c = 0 # 个数
sums = 0 # 总和
for i in range(m,n+1): # 包含n
    if i%2==0: # 被2整除即为偶数 奇数!=0
        print(i)# 逐行打印输出
        c += 1
        sums += i
print(c)
print(sums)





        
