# 优先偶数的TopN

nums = input().split(',')  # type: string
last_str = nums.pop()
last_list = last_str.split(';')
nums.append(last_list[0])
n = int(last_list[1])
nums = list(map(int, nums))
odd_list = []
even_list = []
res = []
for num in nums:
    if num % 2:
        odd_list.append(num)
    else:
        even_list.append(num)
odd_list.sort()
even_list.sort()
for i in range(n):
    if even_list:
        res.append(even_list.pop())
        continue
    else:
        res.append(odd_list.pop())
        continue
res = list(map(str, res))
print(','.join(res))
