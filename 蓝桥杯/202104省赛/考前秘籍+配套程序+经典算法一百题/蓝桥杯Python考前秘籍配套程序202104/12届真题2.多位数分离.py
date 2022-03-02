
#题目：输入整数，输出奇数数字（从个位开始）
ss = input()
lst = []

for i in range(len(ss)):
    if int(ss[i])%2 != 0:
        lst.append(ss[i])
# 反转
lst.reverse()
for i in range(len(lst)):
    print(lst[i])


# 反转方法2
'''
for i in range(len(lst)-1, -1, -1):
    print(lst[i])
'''

# 延伸拓展
'''
c语言分离n各个位数的方法：
个 十 百 千分别用：
n//1%10, n//10%10, n//100%10, n//1000%10
'''
    
