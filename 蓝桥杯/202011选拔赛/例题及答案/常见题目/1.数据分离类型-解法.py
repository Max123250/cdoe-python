s = input()
nums = list(eval(s))
print(nums)
m1 = max(nums)
m2 = min(nums)
sums = 0
for i in range(len(nums)):
    sums += nums[i]
print(m1,m2,sums/5)



#输入n个数据（2<=n<=15，每个数据用','分隔，输出输入了几个数，
#最大数，最小数，由小到大排序）

a = input(':')
lst = a.split(',')
b = []
#转换类型
for i in lst:
    i = int(i)
    b.append(i)

print(lst)
print(b)
print(len(b))
print(max(b))
print(min(b))
b.sort()
print(b)
    
