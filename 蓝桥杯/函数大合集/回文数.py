def fun(a):
    #检测a是否为回文数
    #返回布偶值：True/False(True为回文数/False不为回文数)
    r = False
    b = str(a)
    c = b[::-1]
    if c == b:
        r = True
    return r
'''测试通过'''