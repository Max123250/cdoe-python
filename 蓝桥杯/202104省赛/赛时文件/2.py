'''题目描述：
编程实现：
给定一个正整数N，计算出1到N之间所有奇数的和。

输入描述
输入一个正整数N
输出描述
输出1到N之间（包含1和N）所有奇数的和

样例输入
5
样例输出
9

提示
评分标准：
10分：能正确输出一组数据；
10分：能正确输出两组数据；
20分：能正确输出三组数据。
'''
def fun(a):
    #检测a是否为奇数/偶数
    #返回布偶值：Ture/False(Ture为奇数,False为偶数)
    r = True
    if a%2 == 0:
        r = False
    return r
n = int(input())
lst = []
all = 0
for i in range(1,n+1):
    if fun(i):
        lst.append(i)

for x in lst:
    all += x
print(all)