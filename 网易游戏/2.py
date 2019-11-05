[n, m] = list(map(int, input().split()))
dic_factorial = {}
temp = 1
for i in range(n+1):
    if i <= 1:
        dic_factorial[i] = 1
    else:
        temp *= i
        dic_factorial[i] = temp
if m == n:
    print(dic_factorial[m])
else:
    dp = [0 for i in range(n)]
    for i in range(m):
        dp[i] = dic_factorial[i+1]
    for i in range(m, n):
        dp[i] = dp[i-1] * m ** 2
    print(dp[-1])