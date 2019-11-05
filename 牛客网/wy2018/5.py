# [编程题]重排数列
# 时间限制：1秒
# 空间限制：100768K
# 小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
# 牛博士给小易出了一个难题:
# 对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
# 小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。
#
# 输入描述:
#
# 输入的第一行为数列的个数t(1 ≤ t ≤ 10),
# 接下来每两行描述一个数列A,第一行为数列长度n(1 ≤ n ≤ 10^5)
# 第二行为n个正整数A[i](1 ≤ A[i] ≤ 10^9)
#
# 输出描述:
#
# 对于每个数列输出一行表示是否可以满足牛博士要求,如果可以输出Yes,否则输出No。
#
# 输入例子1:
#
# 2
# 3
# 1 10 100
# 4
# 1 2 3 4
#
# 输出例子1:
#
# Yes
# No

t = int(input())


def four_num(array):
    res = 0
    for num in array:
        if not (num % 4):
            res += 1
    return res


def two_num(array, four):
    res = 0
    for num in array:
        if not num % 2:
            res += 1
    return res - four


for i in range(t):
    num = int(input())
    array = list(map(int, input().split(" ")))
    four = four_num(array)
    two = two_num(array, four)
    one = len(array) - four - two
    if not two:
        if one > four + 1:
            print('No')
        else:
            print('Yes')
    else:
        if not two % 2:
            if one > four:
                print('No')
            else:
                print('Yes')
        else:
            if one > four:
                print('No')
            else:
                print(('Yes'))
