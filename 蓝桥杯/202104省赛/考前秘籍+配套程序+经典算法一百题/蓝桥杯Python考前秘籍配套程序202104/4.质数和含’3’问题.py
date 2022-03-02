# 如果是质数返回True,否则返回False
def fun(a):# 有质数相关问题都可以用这个函数
    r = True
    for i in range(2,a):
        if a%i == 0:
            r = False
            break
    return r

# 如果题目m和n是要求输入的，就用input
m = 1    #int(input())
n = 1000 #int(input())
for i in range(m, n+1):
    if "3" in str(i):# 含3  
        if "33" in str(i): # 含33
            if fun(i):# 如果是质数
                print("&"+str(i)+"*")
            else:
                print("&"+str(i))           
        else:
            print(i)
            
        
