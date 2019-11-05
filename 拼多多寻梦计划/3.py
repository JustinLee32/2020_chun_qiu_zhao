# 3. 骰子期望


# def calc(nums, probe, now):
#     res = 1
#     for i in range(len(nums)):
#         if i < probe:
#             res *= nums[i]
#         else:
#
#
#     return res


n = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()
total = 1
size = len(nums)
for num in nums:
    total *= num
now = 1
res = 1 / total
probe = 0
while now < nums[-1]:
    now += 1
    jishu = 1
    for i in range(len(nums)):
        jishu *= nums[i]
    jishu -= (now-1) ** len(nums)
    res += (now * jishu / total)
print('%.2f' % res)