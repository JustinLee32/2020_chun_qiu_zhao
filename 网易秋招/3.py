def _jump(heights, now, k):
    flag = 1
    temp_list = heights[now+1:now+k+1]
    if max(temp_list) > heights[now]:
        flag = 0
        for i in range(now+1, now+k+1):
            if heights[i] > heights[now]:
                to = i
                break
            else:
                continue
        return to, flag
    else:
        index_list = list(range(now+1, now+k+1))
        temp_list = list(zip(temp_list, index_list))
        temp_list.sort(key=lambda x: (-x[0], -x[1]))
        return temp_list[0][1], flag


def _chao(heights, now, k):
    temp_list = heights[now + 1:now + k + 1]
    index_list = list(range(now + 1, now + k + 1))
    temp_list = list(zip(temp_list, index_list))
    temp_list.sort(key=lambda x: (-x[0], -x[1]))
    return temp_list[0][1]


t = int(input())
for _ in range(t):
    [n, k] = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    now = 0
    chao = 0
    while now < n-1 and chao <= 1:
        now, flag = _jump(heights, now, k)
        if flag:
            if chao == 0:
                now = _chao(heights, now, k)
                chao += 1
                continue
            elif chao == 1:
                chao += 1
                continue
    if chao <= 1:
        print("YES")
    else:
        print("NO")
