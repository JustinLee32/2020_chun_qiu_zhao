text1 = input()
text2 = input()
if not text1 or not text2:
    print(0)
else:
    ans = 0
    m = len(text1)
    n = len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0
    print(dp[m][n])
