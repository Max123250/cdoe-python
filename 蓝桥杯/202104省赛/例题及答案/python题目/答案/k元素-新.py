n = int(input())
k = int(input())
c = 0
if k > n + 1:
    print(c)
else:
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if i + j == k and i != j:
                c += 1
    print(c // 2)
