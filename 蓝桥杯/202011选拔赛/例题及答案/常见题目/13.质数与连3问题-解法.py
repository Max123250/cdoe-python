# 如果是质数返回True,否则返回False
def fun(a):
    r = True
    for i in range(2,a):
        if a%i == 0:
            r = False
            break
    return r

a = int(input(":"))
b = int(input(":"))
for i in range(a, b+1):
    if "3" in str(i):  
        if "33" in str(i):
            if fun(i):# 如果是质数
                print("&"+str(i)+"*")
            else:
                print("&"+str(i))           
        else:
            print(i)
            
        
