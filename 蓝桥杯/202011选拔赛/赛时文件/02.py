#第二题： 输入整数，输出奇数位数字（从个位算起）
num = input()
nums = list(num)
list = []
l = 0
for i in range(len(nums)):
    if len(nums)%2 != 0:
        if i%2 == 0:
            list.append(i)
    else:
        if i%2 != 0:
            list.append(i)

list.reverse()
for l in list:
    print(nums[l])
#20分满分