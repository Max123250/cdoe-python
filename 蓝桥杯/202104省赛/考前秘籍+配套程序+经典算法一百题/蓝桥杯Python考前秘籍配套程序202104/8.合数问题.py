# 题目有要求输入提示语
m = int(input("请输入一个3-100之间的正整数:"))
n = 4 # 从4开始累计
while True: # 双重循环遍历找出满足要求的最小合数
    ss = 0
    for i in range(1,n+1):
        if n%i == 0:
            ss += 1
    if ss == m:
        break
    else:
        n += 1
print(f"具有{m}个不同因数的最小合数是:{n}")
