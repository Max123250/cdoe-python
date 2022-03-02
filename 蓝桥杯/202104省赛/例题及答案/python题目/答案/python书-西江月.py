x = 1
y = x - 18
while True:
    if x + 9 == 2 * (y - 9):
        break
    else:
        x += 1
        y = x - 18
print("x=" + str(x))
print("y=" + str(y))
