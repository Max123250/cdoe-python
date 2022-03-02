lst = ["A","B","C","D"]
all = []
for x in lst:
    for y in lst:
        for z in lst:
            word = x + y + z
            if x != y and y != z and x != z:
                print(word)
                all.append(word)
print(len(all))
