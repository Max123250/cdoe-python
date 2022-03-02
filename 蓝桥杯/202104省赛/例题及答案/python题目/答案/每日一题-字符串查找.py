key = input()
se = input()
num_meny = 1
first_index = 0
start = 0
first_index = se.find(key,start)
start = se.find(key,start)
while True:
    if start != -1:
        start = se.find(key,start)
        num_meny += 1
    else:
        break
if first_index != -1:

