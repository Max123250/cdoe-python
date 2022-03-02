'''
a = [3,10,5,16,8,4]
i = len(a)-1
while i >= 1:
     if a[i-1] < a[i]:
         a[i],a[i-1]=a[i-1],a[i]
     i -= 1
print(a[0])


furits = ["banana","grape","apple","orange","pear"]
j = 1
while j <= len(furits) -1:
    i = len(furits) -1
    while i >= j:
        if furits[i] < furits[i-1]:
            furits[i],furits[i-1] = furits[i-1],furits[i]
        i -= 1
    print(j,furits)
    j += 1
'''

a = [12,6,3,10,5,16,3,4,2,1]
j = 1
while j <= len(a)-1:
    i = len(a)-1
    swap = False
    while i >= j:
        if a[i] > a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
            swap = True
        i -= 1
    if not swap:
        break
    print(j,a)
    j += 1

