feibo = [1,1]
i = 2
while True:
    fn = feibo[i-1] + feibo[i-2]
    if len(feibo) <= 29:
        feibo.append(fn)
        i += 1
    else:
        feibo30rd = feibo.pop()
        break
print(feibo[-1])