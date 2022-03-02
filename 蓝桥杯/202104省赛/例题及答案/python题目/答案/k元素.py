num = int(input())
k = int(input())
all_num = list(range(1,num + 1))
end_num = []
index = 0
plus_num = 1
plus_index = index + plus_num
plus_end = 0
while True:
    while True:
        plus_end = all_num[index] + all_num[plus_index]
        if plus_end == k:
            end_num.append(plus_end)
        plus_index += 1
        print(plus_index)
        if plus_index == num:
            plus_num = 1
            break
    index += 1
print(len(end_num))