num = int(input())
l = list(range(num))
j = 0
while len(l) == 1:
    for i in l:
        if j == 3:
            l.remove(i)
        else:
            j += 1
print("".join(l))
