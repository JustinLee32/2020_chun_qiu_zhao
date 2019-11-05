# 车辆过桥
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 有 N 辆车要陆续通过一座最大承重为 W 的桥，其中第 i 辆车的重量为 w[i]，通过桥的时间为 t[i]。要求： 第 i 辆车上桥的时间不早于第 i - 1 辆车上桥的时间；
#
# 任意时刻桥上所有车辆的总重量不超过 W。
#
# 那么，所有车辆都通过这座桥所需的最短时间是多少？
#
# 输入
# 第一行输入两个整数 N、W（1 <= N、W <= 100000）。第二行输入 N 个整数 w[1] 到 w[N]（1 <= w[i] <= W）。
# 第三行输入 N 个整数 t[1] 到 t[N]（1 <= t[i] <= 10000）。
#
# 输出
# 输出一个整数，表示所有车辆过桥所需的最短时间。


[n, w] = list(map(int, input().split()))
weights = list(map(int, input().split()))
cache = list(weights)
times = list(map(int, input().split()))
times = list(zip(times, list(range(n))))
times = [list(time) for time in times]
ans = 0
bridge_time = []
bridge_weight = 0
while times:
    if weights[0] + bridge_weight <= w:
        bridge_weight += weights.pop(0)
        bridge_time.append(times.pop(0))
    else:
        break
bridge_time.sort(key=lambda x: x[0], reverse=True)
while times:
    temp = bridge_time.pop()
    bridge_weight -= cache[temp[1]]
    ans += temp[0]
    for i in range(len(bridge_time)):
        bridge_time[i][0] -= temp[0]
    while times:
        if weights[0] + bridge_weight <= w:
            bridge_weight += weights.pop(0)
            bridge_time.append(times.pop(0))
        else:
            break
    bridge_time.sort(key=lambda x: x[0], reverse=True)
if bridge_time:
    ans += bridge_time[0][0]
print(ans)
