
#输入明文
text = input()

#凯撒加密
s = ''
i = 0
while i < len(text):
    c = text[i]
    if 'a' <= c <= 'w' or 'A' <= c <= 'W':
        c = chr(ord(c) + 3)
    elif 'x' <= c <= 'z' or 'X' <= c <= 'Z':
        c = chr(ord(c) - 23)
    s = s + c
    i = i + 1
    
#输出密文   
print(s)
