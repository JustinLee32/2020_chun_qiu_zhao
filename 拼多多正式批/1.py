[n, m] = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()
ans = 0
times = 1
if m == 0:
    print(ans)
else:
    while times <= m:
        left = nums.pop(0)
        right = nums.pop()
        ans += left * right
        times += 1
    print(ans)
