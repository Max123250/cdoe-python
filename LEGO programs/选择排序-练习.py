'''
a = [9,28,14,7,22,11]
p = 0
i = p+1
while i < len(a):
    if a[i] > a[p]:
        p = i
    i += 1
print(a[p])

fruits = ["banana","grape","apple","orange","pear"]
j = 0
while j < len(fruits)-1:
    p = j
    i = j+1
    while i < len(fruits):
        if fruits[i] > fruits[p]:
            p = i
        i += 1
    if p != j:
        fruits[j],fruits[p] = fruits[p],fruits[j]
    print(j+1,fruits)
    j += 1
'''
a = [5,16,8,4,2,1]
for j in range(len(a)-1):
    p = j
    for i in range(j,len(a)):
        if a[i] < a[p]:
            p = i
    if p != j:
        a[j],a[p] = a[p],a[j]
    print(j+1,a)