s = input()
num=[]
text=[]
for i in s:
    if "0" <= i <= "9":
        num.append(i)
    elif "A" <= i <= "Z":
        text.append(i)
    elif "a" <= i <= "z":
        text.append(chr(ord(i)-32))
n = len(set(num))**5*len(set(text))
print(n)