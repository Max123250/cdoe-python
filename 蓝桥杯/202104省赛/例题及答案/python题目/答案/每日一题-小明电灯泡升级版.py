light = [0,1,0,1,0,1,0]
index = 0
for i in range(2011):
    if index >= 7:
        index = 0
    if light[index] == 0:
        light[index] = 1
    elif light[index] == 1:
        light[index] = 0
    index += 1
print(light)

