str = input()
num = 0
for x in str:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        num += 1
print(num)
