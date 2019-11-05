def _eat(candies, friend, eaten):
    ans = 0
    k = friend[2]
    now_eat_set = set(range(friend[0], friend[1] + 1))
    can_eat_set = now_eat_set - eaten
    if not can_eat_set:
        ans = -1
    elif len(can_eat_set) <= k:
        eaten = eaten | can_eat_set
        can_eat_list = list(can_eat_set)
        temp_list1 = []
        for i in range(len(can_eat_set)):
            temp_list1.append(candies[can_eat_list[i] - 1])
        temp_list2 = list(zip(temp_list1, can_eat_list))
        temp_list2.sort(key=lambda x: x[0])
        ans = temp_list2[len(can_eat_list)-1][0]
    elif len(can_eat_set) > k:
        can_eat_list = list(can_eat_set)
        temp_list1 = []
        for i in range(len(can_eat_set)):
            temp_list1.append(candies[can_eat_list[i]-1])
        temp_list2 = list(zip(temp_list1, can_eat_list))
        temp_list2.sort(key=lambda x: x[0])
        ans = temp_list2[k-1][0]
        cache = set()
        for i in range(k):
            cache.add(temp_list2[i][1])
        eaten = eaten | cache
    return ans, eaten


[n, m] = list(map(int, input().split()))
candies = list(map(int, input().split()))
eaten = set()
for _ in range(m):
    friend = list(map(int, input().split()))
    ans, eaten = _eat(candies, friend, eaten)
    print(ans)
