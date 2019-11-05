def max_subarray(nums: list) -> int:
    if len(nums) == 0:
        return 0
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)


nums = eval(input())
print(max_subarray(nums))
