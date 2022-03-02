'''
c = 4
def a(n):
    for i in range(3):
        n =(n-1)/3*2
    return (n-1)%3 == 0

while not a(c):
    c += 1
print(c)
'''
c = 4
while True:
    n = c
    for i in range(3):
        n =(n-1)/3*2
    if (n-1)%3 == 0:
        break
    else:
        c += 1
print(c)
