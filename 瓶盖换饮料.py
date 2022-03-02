n = int(input())
g = n#盖子
drink = n#喝的
while g > 3:
    gn = g//3#能换的饮料
    g -= gn*3#减去换饮料用到的盖子
    drink += gn#加上换的饮料
    g += gn#加上换的饮料的盖子
print(drink)
