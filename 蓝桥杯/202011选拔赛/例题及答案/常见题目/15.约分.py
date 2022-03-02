s = input(":")
nums = list(eval(s))
print(str(nums[0])+"/"+str(nums[1]))

a = nums[0]
b = nums[1]

if a >= b:
    for i in range(2,b+1):
        # 可以被一个数一直整除，所以用while不用if
        while a%i==0 and b%i==0:
            a = a//i
            b = b//i
    if b == 1:
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
    
