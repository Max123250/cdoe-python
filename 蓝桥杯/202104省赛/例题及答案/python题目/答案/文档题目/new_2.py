list = list(str(input()))
n_list = []
num_list = [0,0,0,0]
for x in list:
    if "a" <= x <= "z" or "A" <= x <= "z":
        num_list[0] += 1
    elif x == " ":
        num_list[1] += 1
    elif "0" <= x <= "9":
        num_list[2] += 1
    else:
        num_list[3] += 1

for y in num_list:
    print(y)
