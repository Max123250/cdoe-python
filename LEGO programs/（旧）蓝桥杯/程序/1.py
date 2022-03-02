num = input("Enter your number:")
nums = list(eval(num))
nums.sort()
biger_num = nums.pop()
print(biger_num)
print(nums[0])
i_num = 0
for i in nums:
    i_num += i
print(i_num / 5)


max(nums)
min(nums)
nums.sort(reverse = True)
