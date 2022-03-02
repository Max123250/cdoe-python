def fun(a):
    #使用凯撒加密法加密字符串a
    #返回字符串：r(凯撒加密后的a)
    r = ''
    i = 0
    while i < len(a):
        c = a[i]
        if 'a' <= c <= 'w' or 'A' <= c <= 'W':
            c = chr(ord(c) + 3)
        elif 'x' <= c <= 'z' or 'X' <= c <= 'Z':
            c = chr(ord(c) - 23)
        r = r + c
        i = i + 1
    return r
'''测试通过'''