s = input() # 输入两个逗号隔开的数
nums = list(eval(s)) # 装入列表
print(str(nums[0])+"/"+str(nums[1]))

a = nums[0] # 分子
b = nums[1] # 分母
if a >= b: # 分子大于分母
    for i in range(2,b+1):
        # 可以被一个数一直整除，所以用while不用if
        while a%i==0 and b%i==0:
            a = a//i
            b = b//i
    if b == 1: # 分母为1
        print(str(a))
    else:
        print(str(a)+"/"+str(b))
else:
    for i in range(2,nums[0]+1):
        # 可以被一个数一直整除，所以用while不用if
        while a%i==0 and b%i==0:
            a = a//i
            b = b//i
    print(str(a)+"/"+str(b)) 
    
