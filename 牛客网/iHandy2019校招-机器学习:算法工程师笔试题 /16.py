# [编程题]比大更大
# 时间限制：1秒
# 空间限制：32768K
# 给定一列非负整数，求这些数连接起来能组成的最大的数。
#
# 输入描述:
#
# 第一行n>0是一个正整数，表示一共有n个输入。以后每行是一个非负整数，共有n行。
#
# 输出描述:
#
# n个输入的非负整数连接成的最大的数
#
# 输入例子1:
#
# 6
# 9
# 8
# 7
# 65
# 4
# 3
#
# 输出例子1:
#
# 9876543
#
# 输入例子2:
#
# 2
# 11
# 2
#
# 输出例子2:
#
# 211


def add_num(mylist, string):
    res_list = []
    for i in range(len(mylist) + 1):
        temp_list = list(mylist)
        temp_list.insert(i, string)
        res_list.append((int(''.join(temp_list)), i))
    res_list.sort(key=lambda x: x[0], reverse=True)
    mylist.insert(res_list[0][1], string)
    return mylist


num = int(input())
one_list = []
other_list = []
for i in range(num):
    s = input()
    if len(s) == 1:
        one_list.append(s)
    else:
        other_list.append(s)
ans_list = sorted(one_list, reverse=True)
for string in other_list:
    ans_list = add_num(ans_list, string)
print(int(''.join(ans_list)))
