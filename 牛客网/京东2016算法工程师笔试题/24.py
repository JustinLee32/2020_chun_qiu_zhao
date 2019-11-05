# 24/25
# [编程题]上台阶
# 时间限制：3秒
# 空间限制：32768K
# 有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或者二级，要走上m级，共有多少走法？注：规定从一级到一级有0种走法。
# 给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100。为了防止溢出，请返回结果Mod 1000000007的值。
# 测试样例：
# 3
# 返回：2


class GoUpstairs:
    def countWays(self, n):
        if n == 1:
            return 0 % 1000000007
        if n == 2:
            return 1 % 1000000007
        elif n > 2:
            dp = [0 for _ in range(n + 1)]
            dp[0] = 0
            dp[1] = 1
            dp[2] = 1
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n] % 1000000007


if __name__ == '__main__':
    goup = GoUpstairs()
    print(goup.countWays(int(input())))
