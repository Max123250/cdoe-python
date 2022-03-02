a = [7,11,3,2,5]
j = 0
while j < len(a)-1:
    p = j
    i = j+1
    while i < len(a):
        if a[i] < a[p]:
            p = i
        i += 1
    if p != j:
        a[j],a[p] = a[p],a[j]
    print(j+1,a)
    j += 1