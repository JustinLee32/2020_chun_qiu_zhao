m = int(input())
n = int(input())
matrix = []
res = 0
for i in range(m):
    matrix.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(m)]
if n == 1:
    for i in range(1, m):
        res += matrix[i][0]
    print(res)
if m == 1:
    print(sum(matrix[0]))
else:
    dp[-1][-1] = matrix[-1][-1]
    for j in range(n-2, -1, -1):
        dp[-1][j] = dp[-1][j+1] + matrix[-1][j]
    for i in range(m-2, -1, -1):
        dp[i][-1] = dp[i+1][-1] + matrix[i][-1]
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + matrix[i][j]
    print(dp[0][0])