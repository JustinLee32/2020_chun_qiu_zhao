t = int(input())
for _ in range(t):
    [n, m] = list(map(int, input().split()))
    ans = 0
    if not m:
        first = [1 for _ in range(4)]
        second = [0 for _ in range(4)]
        i = 1
        while i < n:
            for j in range(4):
                second[j] = sum(first) - first[j]
            first = list(second)
            second = [0 for _ in range(4)]
            i += 1
        print(sum(first) % 1000000007)
    elif m:
        m_list = list(map(int, input().split()))
        no_task_list = list(map(int, input().split()))
        no_task_dic = dict(zip(m_list, no_task_list))
        first = [0 for _ in range(4)]
        second = [0 for _ in range(4)]
        day = 1
        for j in range(4):
            if day in no_task_dic:
                first[no_task_dic[day] - 1] = 1
                break
            else:
                first[j] = 1
        day += 1
        while day <= n:
            for j in range(4):
                if day in no_task_dic:
                    second[no_task_dic[day] - 1] = sum(first) - first[no_task_dic[day] - 1]
                    break
                else:
                    second[j] = sum(first) - first[j]
            first = list(second)
            second = [0 for _ in range(n)]
            day += 1
        print(sum(first) % 1000000007)

