def f(a):
    r = True
    for i in range(2,a):
        if a % i == 0:
            r = False
            break
    return r
num = []
a = 1
while len(num) <= 10:
    if a % 3 == 2 and a % 7 == 6 and a % 11 == 10 and a % 17 == 16 and a % 23 == 22 and f(a):
        num.append(a)
        print(a)
    a += 1
for x in num:
    print(x)
