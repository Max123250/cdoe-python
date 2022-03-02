list = list(str(input()))
n_list = []
num_list = [0,0,0,0]
for i in range(len(list)):
    n_list.append(ord(list[i]))

for i in range(len(n_list)):
    if 33 < n_list[i] < 47 or 58 < n_list[i] < 64 or 91 < n_list[i] < 96:
        num_list[3] += 1
    elif 65 < n_list[i] < 90 or 97 < n_list[i] < 122:
        num_list[0] += 1
    elif 48 < n_list[i] < 57:
        num_list[2] += 1
    elif n_list[i] == " ":
        num_list[1] += 1
for i in range (len(num_list)):
     print(num_list[i])