'''
无
输出格式
多行输出, 每一行输出一组;
最后一行输出符合要求组合的总数量
'''

n = 0 # 统计满足条件的数的个数
for i in ['A','B','C','D']:
用A,B,C,D四个字母进行组合，三个字母为一组。
组合要求:每组中字母互不相同且每组不重复?总共有多少组?
输入格式
    for j in ['A','B','C','D']:
        for k in ['A','B','C','D']: 
            if i != j and i != k and j != k:
                a = i+j+k # 得到字母组合
                print(a) # 逐个打印满足条件的数
                n = n+1 
print('共有'+str(n)+'个')


        

