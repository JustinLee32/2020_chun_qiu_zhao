def recursive(nums_list, flag):
    if len(nums_list) == 1:
        return nums_list[0]
    res_list = []
    if flag % 2:
        for i in range(0, len(nums_list)-1, 2):
            res_list.append(nums_list[i] | nums_list[i+1])
            flag += 1
    else:
        for i in range(0, len(nums_list)-1, 2):
            res_list.append(nums_list[i] ^ nums_list[i+1])
            flag += 1
    return res_list


[n, m] = list(map(int, input().split()))
nums = list(map(int, input().split()))
operators = []
for _ in range(m):
    operators.append(list(map(int, input().split())))
for operator in operators:
    nums[operator[0]] = operator[1]
    temp = list(nums)
    flag = 1
    while len(temp) > 1:
        temp = list(recursive(temp, flag))
        flag += 1
    print(temp[0])
