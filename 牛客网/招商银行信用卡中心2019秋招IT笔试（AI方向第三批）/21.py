# 21/25
# [编程题]挑选代表
# 时间限制：1秒
# 空间限制：65536K
# 我们有很多区域，每个区域都是从a到b的闭区间，现在我们要从每个区间中挑选至少2个数，那么最少挑选多少个？
#
# 输入描述:
#
# 第一行是N（N<10000）,表示有N个区间，之间可以重复
# 然后每一行是ai,bi，持续N行，表示现在区间。均小于100000
#
# 输出描述:
#
# 输出一个数，代表最少选取数量。
#
# 输入例子1:
#
# 4
# 4 7
# 2 4
# 0 2
# 3 6
#
# 输出例子1:
#
# 4


def operate(temp_list):
    temp_list.sort(key=lambda x: x[1])
    return [temp_list[0]]


def get_count(left, right):
    if left[1] < right[0]:
        return 2
    elif left[1] == right[0]:
        return 1
    elif left[1] > right[0]:
        return 0


n = int(input())
if n <= 1:
    print(2 * n)
else:
    nums_temp_list = []
    nums_list = []
    ans = 0
    for i in range(n):
        nums_temp_list.append(tuple(map(int, input().split())))
    nums_temp_list.sort(key=lambda x: x[0])
    for i in range(n-1):
        j = i + 1
        temp_list = [nums_temp_list[i]]
        while j <= n-1:
            if nums_temp_list[i][0] == nums_temp_list[0]:
                j += 1
                temp_list.append(nums_temp_list[j])
            else:
                temp_list = operate(temp_list)
                break
        temp_list = operate(temp_list)
        nums_list += temp_list
    if len(nums_list) <= 1:
        print(len(nums_list) * 2)
    else:
        for i in range(len(nums_list) - 1):
            ans += get_count(nums_list[i], nums_list[i+1])
        print(ans + 2)
