z = int(input())
if z <= 6:
    print("少发")
elif 7 <= z <= 19:
    print("较易发")
elif 20 <= z <= 30:
    print("易发")
else:
    print("极易发")