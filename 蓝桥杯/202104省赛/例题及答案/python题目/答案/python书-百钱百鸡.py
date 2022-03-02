gj = 0
mj = 0
xj = 0
for xj in range(1, 101):
    for mj in range(1, 101-xj):
        for gj in range(1, 101 - (xj + mj)):
            if xj % 3 == 0:
                if xj/3 + mj*3 + gj*5 == 100 and xj + mj + gj == 100:
                    print("小鸡" + str(xj) + "只")
                    print("母鸡" + str(mj) + "只")
                    print("公鸡" + str(j) + "只")
                    print("\n")

