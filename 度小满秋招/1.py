# 隔山打牛
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# “你可曾听闻一招从天而降大掌法？”
#
#   在一部游戏中有这样一个技能，假设地图是一条直线，长度为n，人物所处的位置是x，则可以对x，2*x和2*x+1三格内的敌人分别造成一点伤害，要求2*x+1<=n。
#
#   设为这个地图的格子做标记为1-n，第i个格子中有一个血量为a_i的敌人。请问你至少使用多少次技能，可以杀死这个地图上所有敌人。
#
# 输入
# 输入第一行包含一个正整数n,表示格子的数量(1<=n<=100)
#
# 输入第二行包含n个正整数a_i,表示第i个格子中敌人的血量。
#
# 输出
# 输出仅包含一个正整数，即至少使用多少次技能。


n = int(input())
bloods = list(map(int, input().split()))
bloods.insert(0, 0)
ans = 0
if n == 1:
    print(bloods[1])
else:
    for i in range(1, n // 2 + 1):
        ans += bloods[i]
        bloods[2 * i] -= min(bloods[i], bloods[2 * i])
        if 2 * i + 1 <= n:
            bloods[2 * i + 1] -= min(bloods[i], bloods[2 * i + 1])
        bloods[i] = 0
    for i in range(1, n // 2 + 1):
        if 2 * i + 1 <= n:
            while bloods[2 * i] and bloods[2 * i + 1]:
                ans += 1
                bloods[2 * i] -= 1
                bloods[2 * i + 1] -= 1
        else:
            continue
    ans += sum(bloods)
    print(ans)
