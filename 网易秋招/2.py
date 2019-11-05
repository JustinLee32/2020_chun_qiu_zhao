t = int(input())
for _ in range(t):
    [n, m] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    need = (n - 1) * n / 2
    have = sum(nums) + m
    if have >= need:
        print("YES")
    else:
        print("NO")
