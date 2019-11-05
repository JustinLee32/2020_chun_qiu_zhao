def compare(string1, string2):
    return True if string1 + string2 >= string2 + string1 else False


nums = list(input().split(','))
res = ''
if len(nums) == 0:
    print(res)
else:
    res += nums[0]
    for i in range(1, len(nums)):
        if compare(res, nums[i]):
            res += nums[i]
        else:
            res = nums[i] + res
    print(res)
