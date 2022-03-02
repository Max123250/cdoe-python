ls = list(eval(input()))
g = 1
i = len(ls) - 1
t = 0
while g <= len(ls) - 1:
    i = len(ls) - 1
    while i >= g:
        if ls[i] < ls[i-1]:
            t = ls[i-1]
            ls[i-1] = ls[i]
            ls[i] = t
        i -= 1
    print(ls)
    g += 1




