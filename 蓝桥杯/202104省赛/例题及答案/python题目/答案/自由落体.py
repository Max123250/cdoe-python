n = int(input())
for i in range(10):
    n = n/2
print(n)

num = 2
a = 0
for i in range(10):
    a = a+n+n/2
    n = n/2
print(a)
