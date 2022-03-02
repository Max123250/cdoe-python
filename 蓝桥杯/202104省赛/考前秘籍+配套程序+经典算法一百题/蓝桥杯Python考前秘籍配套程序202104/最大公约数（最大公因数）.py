def fun(a,b):
    #求出a和b的最大公约数/最大公因数
    #返回数字：r(a和b的最大公约数/最大公因数)
    r = 1
    for i in range(1,b):
        if a % i == 0 and b % i == 0:
            r = i
    return r
'''测试通过'''