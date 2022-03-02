'''题目描述：
编程实现：
有一个N*N的矩阵方格和N个棋子，现在需要将N个棋子按要求放置到矩阵方格中。
要求如下：
                1.任意两个棋子不能在同一行
                2.任意两个棋子不能在同一列
                3.任意两个棋子不能在同一对角线上（下图红色线段都为对角线）
根据以上要求，问N个棋子放置到N*N矩阵方格中有多少种放置方案
例如：4*4的矩阵方格，4个棋子，有2种放置方案
输入一个正整数N(1<N<11)，表示一个N*N的矩阵方格和N个棋子数量
输出描述
输出N个棋子按要求放置到N*N的矩阵方格中有多少种放置方案

样例输入
4
样例输出
2

提示
评分标准：
20分：能正确输出一组数据；
20分：能正确输出两组数据；
20分：能正确输出三组数据；
20分：能正确输出四组数据;
20分：能正确输出五组数据。
'''
'''
zip:zip(list,list)
unzip:zip(*zipped)
'''
def check(y,x):
    for i in range(8):
        if l[i][x] == 1:
            return False

    for j,k in zip(range(y-1,-1,-1),range(x-1,-1,-1)):
        if l[j][k] == 1:
            return False

    for j,k in zip(range(y-1,-1,-1),range(x+1,8)):
        if l[j][k] == 1:
            return False
    return True

def find(y):
    global c
    if y > 7:
        c += 1
        return
    for x in range(8):
        if check(y,x):
            l[y][x] = 1
            find(y+1)
            l[y][x] = 0


a = int(input())
l = [[0 for i in range(a)] for i in range(a)]
c = 0
find(0)
print(c)