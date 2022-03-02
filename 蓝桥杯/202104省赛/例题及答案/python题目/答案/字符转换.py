str_word = input()
list = []
for x in str_word:
    word = None
    if "0" <= x <= "9":
        word = str(ord(x))
    elif "a" <= x <= "z":
        word = x.upper()
    elif "A" <= x <= "Z":
        word = x.lower()
    list.append(word)
print("".join(list))