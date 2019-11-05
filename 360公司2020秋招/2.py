# 散步
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 饭后散步是一个很好的习惯，一天晚上，小A在一条笔直的路上散步，起点在路上某处，但是因为路上没有标识，
# 他并不知道这个起点位于路上的那个位置，现在将道路划分为N-1个等距的部分，你可以把这条路当成一个数轴，
# 道路上的结点标记为1~N，起点和终点只可能是这N个点中的一个。
#
# 但是小A还提供了一个重要信息，他每隔一段时间就会用手机看一下自己走了多远，记作D，但是他并不记得他是朝着哪个方向走的，
# 唯一可以确定的是，在两次看手机的间隔中他不会改变方向，每次看完手机后他可能继续向前或者回头走。
#
# 那么问题来了，已知他在散步过程中始终在1~N的范围内，那么符合上述条件的终点可能有多少个呢？
#
# 输入
# 输入第一行包含一个正整数N，M，N表示道路的长度，也是数轴上点的数量，M是小A提供的D的数量。(N,M<=20000)
#
# 接下来有M行，每行一个正整数D，表示小A朝着某个方向走了D个单位。(D<=20000)
#
# 输出
# 输出仅包含一个整数，表示可能的起点的数量。
#
#
# 样例输入
# 10 3
# 5
# 2
# 6
# 样例输出
# 8


def select(now, step, total):
    if now - step - 1 > total - now - step:
        # 离1远，往正方向走
        return 0
    elif now - step - 1 <= total - now - step:
        # 离1近，往负方向走
        return 1


def is_ok(first, n, steps):
    visited = [[0 for _ in range(m)] for _ in range(n+1)]
    now = first
    for i, step in enumerate(steps):
        if now - step < 1:
            if now + step > n:
                return False
            elif now + step < n:
                if visited[now+step][i]:
                    return False
                visited[now + step][i] = 1
                now += step
                continue
        elif now - step > 1:
            if now + step > n:
                if visited[now-step][i]:
                    return False
                now -= step
                visited[now-step][i] = 1
                continue
            elif now + step < n:
                flag = select(now, step, n)
                if flag:
                    if visited[now-step][i]:
                        if visited[now+step][i]:
                            return False
                        else:
                            visited[now+step][i] = 1
                            now += step
                    else:
                        visited[now-step][i] = 1
                        now -= step
                elif not flag:
                    if visited[now+step][i]:
                        if visited[now-step][i]:
                            return False
                        else:
                            visited[now-step][i] = 1
                            now -= step
                    else:
                        visited[now+step][i] = 1
                        now += step
    return True


[n, m] = list(map(int, input().split()))
steps = []
res = 0
# temp = 0
for i in range(m):
    steps.append(int(input()))
# for i in range(1, n+1):
#     if is_ok(i, n, steps):
#         temp += 1
steps.reverse()
for i in range(1, n+1):
    if is_ok(i, n, steps):
        res += 1
# res = min(temp, res)
print(res)
