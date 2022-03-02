def f(n1,n2,y):
    w = 2
    feibo = [0]*(y+1)
    feibo[0] = 1
    feibo[1] = 1
    while w < y:
        if w == n1 or w == n2:
            feibo[w] = 0
        else:
            feibo[w] = feibo[w-1] + feibo[w-2]
        w += 1
    return feibo[y-1]

l = list(eval(input()))
n1 = l[0]
n2 = l[1]
y = l[2]
print(f(n1,n2,y))