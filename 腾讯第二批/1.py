t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    flag = 1
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for key, value in dic.items():
        if value > n / 2:
            print('NO')
            flag = 0
            break
        else:
            continue
    if flag:
        print('YES')
