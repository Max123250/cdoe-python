'''
公鸡五元一只
母鸡三元一只
小鸡一元三只
'''
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if x * 5 + y * 3 * 1 / 3 == 100:
            print(x,y,z)
   
