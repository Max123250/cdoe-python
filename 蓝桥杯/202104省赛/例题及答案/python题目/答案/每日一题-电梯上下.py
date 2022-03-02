floor = list(eval(input()))
litle = False
floor_num = 0
e = 0
all_e = 0
nr = 0
for i in range(len(floor)-1):
    e = 0
    nr = 0
    f = floor[i]
    l = floor[i+1]

    if f > 0:
        e += 1
    if l > 0:
        e += 1

    if f < l:
        if e != 1:
            nr += (l-f)*1
        else:
            nr += (l-f -1)*1
    else:
        if e != 1:
            nr += (f-l)*0.3
        else:
            nr += (f-l -1)*0.3


    all_e += nr

print(all_e)
