def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
i = 0
feibo = []
while True:
    if 1000 <= f(i) <= 10000:
        feibo.append(f(i))
    elif f(i) > 10000:
        break
    i += 1

for y in feibo:
    print(y)