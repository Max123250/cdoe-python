def fun(a):
    #检测a是否是质数/合数
    #返回布偶值True为质数/False为合数
    r = True
    for i in range(2,a):
        if a%i == 0:
            r = False
            break
    return r
'''测试通过'''