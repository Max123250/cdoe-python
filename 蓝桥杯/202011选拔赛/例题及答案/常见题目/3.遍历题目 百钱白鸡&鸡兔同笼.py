#题目 公鸡5元，母鸡3元，3只小鸡1元，100元买100只鸡

for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if x*5+y*3+z*1/3 == 100:
            print(f'{x},{y},{z}')
    


# 鸡兔同笼 35个头，94条腿

for x in range(1,23):
    y = 35 - x
    if 4*x + 2*y == 94:
        print('兔子有%s只，鸡有%s只'%(x, y))
