# 80%
# 8/8
# [编程题]牛牛的背包问题
# 时间限制：1秒
# 空间限制：32768K
# 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
# 牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
# 牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
#
# 输入描述:
#
# 输入包括两行
# 第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
# 第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。
#
# 输出描述:
#
# 输出一个正整数, 表示牛牛一共有多少种零食放法。
#
# 输入例子1:
#
# 3 10
# 1 2 4
#
# 输出例子1:
#
# 8
#
# 例子说明1:
#
# 三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。


def can_add(element, v, index, w):
    if v[index] > w - element[1]:
        return None
    else:
        return (index, element[1] + v[index])


[n, w] = list(map(int, input().split(" ")))
v = list(map(int, input().split(" ")))
v.sort()
queue = []
if v[0] > w:
    print(1)
else:
    queue.append((1, v[0]))
    queue.append((1, 0))
    for i in range(1, n):
        l = len(queue)
        for j in range(l):
            temp = queue.pop(0)
            queue.append((i+1, temp[1]))
            if can_add(temp, v, i, w):
                queue.append(can_add(temp, v, i, w))
            else:
                pass
    print(len(queue))




