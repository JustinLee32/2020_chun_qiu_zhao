# 31/32
# [编程题]矩阵查数
# 时间限制：4秒
# 空间限制：65536K
# 给定一个二维整型矩阵，已知矩阵的每一行都按照从小到大的顺序排列，每一列也都按照从小到大的顺序排列。现在给出一个数，请写一个函数返回该数是否存在于矩阵中。
# 矩阵中出现的数字与需要查找的数(k)都为0~100000之间的整数，且矩阵的大小在3000*3000以内。
# 在保证正确性的基础上，请尽量给出比较高效的解法。请列出你的算法时间复杂度与空间复杂度分别是多少？
#
#
# 输入描述:
#
# 输入两个整数m,n, 且 0<m<=3000, 0<n<=3000。
#
# 接着输入一个vector<vector<int>> matrix矩阵，大小为m行n列，与一个int k，为需要查找的数字。
#
# 输出描述:
#
# 输出true或者false，true表示该数k存在于该matrix矩阵中，false表示该数k不存在于该matrix矩阵中。
#
# 输入例子1:
#
# 3 3
# ​​2 3 5
# ​​3 4 7
# ​​3 5 8
# 4
#
# 输出例子1:
#
# true
#
# 例子说明1:
#
# 4位于矩阵的第二行第二列，故输出true


[m, n] = list(map(int, input().split(" ")))
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split(" "))))
target = int(input())
if m == 1:
    if target in matrix[0]:
        print('true')
    else:
        print('false')
elif n == 1:
    flag = 0
    for i in range(m):
        if target == matrix[i][0]:
            print('true')
            flag = 1
            break
        else:
            continue
    if not flag:
        print('false')
else:
    flag = 0
    for i in range(m):
        if matrix[i][0] > target:
            break
        elif matrix[i][0] == target:
            print('true')
            flag = 1
            break
        else:
            if matrix[i][n-1] < target:
                continue
            elif matrix[i][n-1] == target:
                print('true')
                flag = 1
                break
            else:
                left = 0
                right = n-1
                while left < right - 1:
                    mid = int((left + right) /2)
                    if matrix[i][mid] == target:
                        print('true')
                        flag = 1
                        break
                    elif matrix[i][mid] > target:
                        right = mid
                        continue
                    else:
                        left = mid
                        continue
                if not flag:
                    continue
                else:
                    break
