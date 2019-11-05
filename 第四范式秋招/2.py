def maximal_square(m, n, matrix) -> int:
    if m == 0 or n == 0:
        return 0
    dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
    if m <= 1 or n <= 1:
        dp_2 = [[int(matrix[i][j]) for i in range(m)] for j in range(n)]
        return max(max(dp[0]), max(dp_2[0]))
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j] * (1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]))
    # dp[i][j]表示以matrix[i][j]为正方形的右下角顶点所能够构成的最大正方形的边长
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dp[i][j])
    return res * res


[m, n] = list(map(int, input().split(',')))
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split(','))))
print(maximal_square(m, n, matrix))
