n = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    ans = ans ^ num
print(ans)