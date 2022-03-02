'''题目描述：
有一个密室逃脱游戏，有100间密室连在一排。密室编号是从1开始连续排列一直排到第100间密室，如下图：
游戏规则：
1. 玩家初始位置在1号密室；
2. 每次玩家可以进入右边的一个密室，也可以跳过一个密室进入下个密室（如：当玩家当前在3号密室，他可以进入4号密室也可以进入5号密室）;
3. 有毒气的密室不能进入需要避开。

编程实现：
给定三个正整数X，Y，M（1<X<Y<M≤100），表示三个密室编号。X号密室和Y号密室有毒气泄漏，不能进入，玩家需要进入到M号密室。按照游戏规则进入M号密室有多少种路线方案。
例如：X=2，Y=4，M=7，2号和4号有毒气泄露，避开2号和4号毒气密室，进入7号密室有2种路线方案，分别是1->3->5->6->7路线和1->3->5->7路线。

输入描述
输入三个正整数X，Y，M（1<X<Y≤M），并以英文逗号隔开
输出描述
输出从1号密室开始避开X、Y号毒气密室，进入M号密室有多少种路线方案

样例输入
2,4,7
样例输出
2

评分标准：
20分：能正确输出一组数据；
20分：能正确输出两组数据；
20分：能正确输出三组数据；
20分：能正确输出四组数据。
'''
import random
nums = list(eval(input()))
now_ms = 1
n_ms1 = int(nums[0])
n_ms2 = int(nums[1])
y_ms = int(nums[2])
ms_all = []
ms_a_all = [1]
new_ms_all = []
can = False
for i in range(100):
    can = False
    now_ms = 1
    ms_a_all = [1]
    while True:
        if n_ms1 == now_ms+1 or n_ms2 == now_ms+1:
            now_ms += 2
        elif n_ms1 == now_ms+2 or n_ms2 == now_ms+2:
            now_ms += 1
        elif not n_ms1 == now_ms+1 or not n_ms2 == now_ms+1 or not n_ms1 == now_ms+2 or not n_ms2 == now_ms+2:
            n = random.randint(1,2)
            now_ms += n
        ms_a_all.append(now_ms)
        if int(now_ms) == y_ms:
            if not n_ms1 in ms_a_all or not n_ms2 in ms_a_all:
                can = True
                break
        elif now_ms > y_ms:
            break
    if can:
        if not ms_a_all in ms_all:
            ms_all.append(ms_a_all)
for x in ms_all:
    for y in x:
        if int(y) != int(n_ms1) and int(y) != int(n_ms2):
            if not x in new_ms_all:
                new_ms_all.append(x)
print(len(new_ms_all))
