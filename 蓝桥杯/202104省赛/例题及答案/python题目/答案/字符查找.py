s1 = input("1:")
s2 = input("2:")
s3 = input("3:")
all_s = s1+s2+s3

letter_none = list(set(all_s))
letter = []
for x in all_s:
    x = x.upper()
    if not x in letter:
        if "A" <= x <= "Z":
            letter.append(x)
letter.sort()

num = []
n = 0
for y in letter:
    n = all_s.upper().count(y)
    num.append(str(n))

print(all_s)
print("    ".join(letter))
print("    ".join(num))
