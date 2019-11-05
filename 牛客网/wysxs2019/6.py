# 50%
# 6/8
# [编程题]矩形重叠
# 时间限制：1秒
# 空间限制：32768K
# 平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。
# 如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。
# 请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。
#
# 输入描述:
#
# 输入包括五行。
# 第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
# 第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
# 第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
# 第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
# 第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。
#
# 输出描述:
#
# 输出一个正整数, 表示最多的地方有多少个矩形相互重叠,如果矩形都不互相重叠,输出1。
#
# 输入例子1:
#
# 2
# 0 90
# 0 90
# 100 200
# 100 200
#
# 输出例子1:
#
# 2


def check(queue):
    if len(queue) <= 1:
        return queue
    temp_list = queue[:-1]
    temp_list.sort(reverse=False, key=lambda x: x[1])
    for i in range(len(queue)-2, -1, -1):
        low = queue[i][1]
        up = queue[-1][0]
        if low > up:
            continue
        elif low <= up:
            return queue[i+1:]
    return queue


num = int(input())
l_b_x = list(map(int, input().split()))
l_b_y = list(map(int, input().split()))
r_u_x = list(map(int, input().split()))
r_u_y = list(map(int, input().split()))
temp_x = []
temp_y = []
for i in range(num):
    temp_x.append((l_b_x[i], r_u_x[i]))
    temp_y.append((l_b_y[i], r_u_y[i]))
temp_x.sort(key=lambda x: x[0])
temp_y.sort(key=lambda y: y[0])
queue_x = []
queue_y = []
flag_1 = 0
flag_2 = 0
for i in range(num):
    queue_x.append(temp_x[i])
    queue_y.append(temp_y[i])
    queue_x = check(queue_x)
    queue_y = check(queue_y)
    flag_1 = max(flag_1, len(queue_x))
    flag_2 = max(flag_2, len(queue_y))
print(min(flag_1, flag_2))
