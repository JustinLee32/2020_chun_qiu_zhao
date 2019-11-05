# 23/25
# [编程题]目的地最短步数
# 时间限制：1秒
# 空间限制：32768K
# 考虑你从家出发步行去往一处目的地，该目的地恰好离你整数单位步长（大于等于1）。你只能朝向该目的地或者背向该目的地行走，
# 而你行走的必须为单位步长的整数倍，且要求你第N次行走必须走N步。
# 请就给出目的地离你距离，判断你是否可以在有限步内到达该目的地。如果可以到达的话，请计算到达目的地的最短总步数(不能到达则输出-1)。
#
# 输入描述:
#
# 1个整数：目的地离你距离T
#
# 输出描述:
#
# 1个整数：最短总步数（进行了多少次行走）
#
# 输入例子1:
#
# 2
#
# 输出例子1:
#
# 3
#
# 例子说明1:
#
# 距离目的地2， 需要3步：朝向走1，背向走2，朝向走3

target = int(input())
target = abs(target)
if target == 0:
    print(0)
else:
    step = 0
    ans = 0
    sum = 0
    i = 1
    while True:
        sum += i
        step += 1
        if sum == target:
            print(step)
            break
        elif sum < target:
            i += 1
            continue
        elif sum > target:
            if (sum + target) % 2:
                i += 1
                continue
            else:
                print(step)
                break
