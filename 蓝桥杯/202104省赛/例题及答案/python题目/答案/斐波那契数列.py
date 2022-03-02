f = [1,1]
new_f = []
i = 2
while True:
    fn = f[i-1] + f[i-2]
    if fn <= 10000:
        f.append(fn)
        i += 1
    else:
        break
for x in f:
    if x >= 1000:
        new_f.append(x)
for y in new_f:
    print(y)
print("1000至10000之间有个数为:{}".format(str(len(new_f))))