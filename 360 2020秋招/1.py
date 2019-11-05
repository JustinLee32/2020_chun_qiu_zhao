# 表面积
# # 时间限制：C/C++语言 1000MS；其他语言 3000MS
# # 内存限制：C/C++语言 65536KB；其他语言 589824KB
# # 题目描述：
# # 将长N*M厘米的矩形区域划分成N行M列（每行每列的宽度均为1厘米），在第i行第j列的位置上叠放Ai,j个边长为1厘米的正方体（1≤Ai,j≤100），所有正方体就组成了一个立体图形，每个正方体六个面中的一部分会被其它正方体遮挡，未被遮挡的部分的总面积即为该立体图形的表面积，那么该立体图形的表面积是多少平方厘米？
# #
# # 样例解释：
# #
# #
# #
# # 输入
# # 第一行包含两个整数N和M，1≤N，M≤1000。
# #
# # 接下来N行，每行包含M个整数，第i行的第j个整数表示Ai,j。
# #
# # 输出
# # 输出表面积的大小。
# #
# #
# # 样例输入
# # 2 2
# # 2 1
# # 1 1
# # 样例输出
# # 20


def get_max(matrix, n, m, j):
    temp = []
    for i in range(n):
        temp.append(matrix[i][j])
    return max(temp)


def get_more(my_list):
    res = 0
    temp = []
    temp.append(my_list[0])
    stage = 0
    i = 1
    while i < len(my_list):
        if stage == 0:
            if my_list[i] >= temp[0]:
                temp.pop(0)
                temp.append(my_list[i])
                i += 1
            elif my_list[i] < temp[0]:
                stage = 1
                temp.append(my_list[i])
                i += 1
                continue
        elif stage == 1:
            if my_list[i] <= temp[1]:
                temp.pop(1)
                temp.append(my_list[i])
                i += 1
            elif my_list[i] > temp[1]:
                stage = 2
                temp.append(my_list[i])
                i += 1
                continue
        elif stage == 2:
            if my_list[i] >= temp[2]:
                temp.pop(2)
                temp.append(my_list[i])
                i += 1
            elif my_list[i] < temp[2]:
                stage = 1
                temp.append(my_list[i])
                i += 1
                res += min(temp[0], temp[2]) - temp[1]
                temp = []
                continue
    return res



[n, m] = list(map(int, input().split()))
if n * m == 0:
    print(0)
else:
    matrix = []
    for i in range(n):
        matrix.append((list(map(int, input().split()))))
    ans = 0
    ans += 2 * m * n

    left = 0
    for i in range(n):
        left += max(matrix[i])

    right = left

    behind = 0
    for j in range(m):
        temp = get_max(matrix, n, m, j)
        behind += temp

    front = behind

    more_1 = 0
    if n < 3:
        pass
    else:
        for i in range(n):
            more_1 += get_more(matrix[i])

    more_2 = 0
    if m < 3:
        pass
    else:
        for j in range(m):
            temp_list = []
            for i in range(n):
                temp_list.append(matrix[i][j])
                more_2 += get_more(temp_list)
    ans = ans + left + right + behind + front + more_1 + more_2
    print(ans)
