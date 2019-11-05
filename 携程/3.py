# 旅游路线设计
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 用户出行旅游通常都是一个闭环，即从某地出发游览各个景点，最终回到出发地。已知各个景点间的通行时间。
# 请你设计一套算法，当用户给定出发地以及景点后，给出一条游览路线，使得用户能够不重复的游历每个景点并返回出发地的总通行时间最短，计算该最短通行时间。
# 假设所有用户的出发地都是0
#
# 输入
# 第一行：出发地与景点的总个数 n
#
#
# 第二行：景点间的直达路线的个数m
#
#
# 其后m行：各个景点的通行时间a   b   t
#
# 表示a地与b地之间的通行时间是t。
#
# 输出
# 不重复游览完所有景点并返回出发地的最短游览时间T
#
# 若不存在这样的游览路线，返回-1
#
#
# 样例输入
# 4
# 6
# 0 1 4
# 0 2 3
# 0 3 1
# 1 2 1
# 1 3 2
# 2 3 5
# 样例输出
# 7

n = int(input())
m = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    temp_list = list(map(int, input().split()))
    i = temp_list[0]
    j = temp_list[1]
    time = temp_list[2]
    matrix[i][j] = matrix[j][i] = time

visted = []
res = 0


def helper(matrix, visted, now, temp):
    global res
    if len(visted) == n:
        if not res:
            res = temp + matrix[now][0]
        else:
            res = min(res, temp+matrix[now][0])
        return
    else:
        for i in range(n):
            if matrix[now][i] and i not in visted:
                helper(matrix, visted + [i], i, temp + matrix[now][i])


helper(matrix, visted, 0, 0)
print(res)
