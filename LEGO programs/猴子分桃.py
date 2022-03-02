c = 6
while True:
    n = c
    for i in range(4):
        n =(n-1)/5*4
    if (n-1)%5 == 0:
        break
    else:
        c += 1
print(c)
