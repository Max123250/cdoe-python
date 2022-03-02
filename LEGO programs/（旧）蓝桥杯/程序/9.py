num = [0,0,0]
all_num = []
for i_1 in range(4):
    for i_3 in range(4):
        for i_5 in range(4):
            for i_8 in range(4):
                if i_1 + i_3 + i_5 + i_8 == 3:
                    if not i_1 == 3:
                        num[i_1] = i_1
                    elif not i_3 == 3:
                        num[i_3] = i_3
                    elif not i_5 == 3:
                        num[i_5] = i_5
                    elif not i_8 == 3:
                        num[i_8] = i_8
                    print(num)
                    if not num in all_num:
                        all_num.append(num)
print(all_num)