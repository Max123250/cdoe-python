x = int(input())
y = int(input())
z = int(input())
nums = [] # 定义空列表
nums.append(x) # 将数字装入列表
nums.append(y)
nums.append(z)
nums.sort() # 从小到大排序
# 逐个输出
print(nums[0])
print(nums[1])
print(nums[2])
