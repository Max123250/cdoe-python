import random
y_cp = input("彩票号：")
x_cp = random.randint(10000,99999)
money = 0
if y_cp == str(x_cp):
    money = 10000
else:
    for x in list(y_cp):
        if x in str(x_cp):
            money += 1000
print("彩票号：",x_cp)
print("奖金：",money)