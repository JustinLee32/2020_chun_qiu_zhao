# def add_targets(targets: list, new: list) -> list:
#     return list(set(targets) | set(new))
#
#
# def creat_list(intersection: set) -> list:
#     return list(range(intersection[0], intersection[1] + 1))
#
#
# [n, m] = list(map(int, input().split()))
# doors = []
# balls = []
# ans = 0
# for i in range(n):
#     doors.append(list(map(int, input().split())))
# for i in range(m):
#     balls.append(int(input()))
# doors.sort(key=lambda x: (x[0], x[1]))
# targets = []
# targets += list(creat_list(doors[1]))
# for i in range(1, len(doors)):
#     targets = add_targets(targets, creat_list(doors[i]))
# targets = set(targets)
# for ball in balls:
#     if ball in targets:
#         ans += 1
# print(ans)

# 题目描述：
# 在一档综艺节目中，有一个定点射门的游戏，在一条直线上有n个球门区域，这些球门的大小并不一样，
# 用形如“a b”的方式表示，球门区域是从a坐标到b坐标的区域，另外在距离球门所在直线不远处的平行轴处，
# 有若干个摆放好的足球，由于参加综艺的人并不是专业运动员，因此只会将该直线a坐标处的足球踢到另一条直线的a坐标处。
#
# 球门可能会有重合，对于任何一个重合的位置，你可以任选一个球门踢入。只要有一个球门内有进球，就可以加一分，这位选手最多可以得多少分。
#
# 一颗球不可以在两个球门中重复计数，门柱等问题忽略不计。
from collections import defaultdict
doors = []
balls = []
ans = 0
[n, m] = list(map(int, input().split()))
for _ in range(n):
    doors.append(list(map(int, input().split())))
for _ in range(m):
    balls.append(int(input()))
doors.sort(key=lambda x: (x[0], x(1)))
balls.sort()

