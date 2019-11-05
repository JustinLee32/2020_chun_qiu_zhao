def num_squares(n: int) -> int:
    dp = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        j = 1
        while i - j * j >= 0:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


n = int(input())
print(num_squares(n))
