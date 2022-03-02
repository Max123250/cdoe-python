def fun(a,b):
    #求出a和b的最小公倍数
    #返回数字：r(a和b的最小公倍数)
    if a > b:
        m = a
    else:
        m = b
    r = m  # 公倍数
    for i in range(m,a*b+1):
        if i % a == 0 and i % b == 0:
            r = i
            break  # 找到即可退出，因为要找最小
    return r
'''测试通过'''