str = input()
jm = []
for x in str:
    word = x
    if "a" <= x <= "x" or "A" <= x <= "X":
        if "a" <= x <= "w" or "A" <= x <= "W":
            word = chr(ord(x) + 3)
        elif "x" <= x <= "z" or "X" <= x <= "Z":
            word = chr(ord(x) - 23)
    jm.append(word)
print("".join(jm))
