# 输入n个数，转成列表处理
s = input() # 输入逗号隔开的n个数
nums = list(eval(s)) # 存在列表中
m1 = max(nums) # 最大 
m2 = min(nums) # 最小
print(m1)
print(m2)

# 求平均值
sums = 0
for i in range(len(nums)):# len:列表元素个数
    sums += nums[i]
print(sums/len(nums))

