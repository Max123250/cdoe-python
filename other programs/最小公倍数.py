num1 = int(input("输入数字1："))
num2 = int(input("输入数字2："))
num_times = 1
num1l = []
num2l = []
while True:
    num1l.append(num1)
    num2l.append(num2)
    num1 = num1*num_times
    num2 = num2*num_times
    num2l_pop = num2l.pop
    if num2 in num1l:
        print("它们的公倍数是：",num2)
    num_times = num_times + 1