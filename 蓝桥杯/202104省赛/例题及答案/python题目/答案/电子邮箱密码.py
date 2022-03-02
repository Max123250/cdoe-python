key_word = []
for i in range(310000,320000):
    if str(i)[4] == str(i)[5]:
        if i % 16 == 0 and i % 46 == 0:
            key_word.append(i)
            print(i)
print(len(key_word))
