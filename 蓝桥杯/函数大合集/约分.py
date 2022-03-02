def fun(a,b):
    #检测分子a与分母b能否约分
    #返回列表：[a,b](可以约分则返回约分后的a、b，不行则保持不变）
    if a >= b:
        for i in range(2,b+1):
            while a%i == 0 and b%i == 0:
                a = a//i
                b = b//i
    else:
        for i in range(2,a+1):
            while a%i == 0 and b%i == 0:
                a = a//i
                b = b//i
    return [a,b]
'''测试通过'''