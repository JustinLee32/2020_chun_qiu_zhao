# AC
# 7/8
# [编程题]牛牛的闹钟
# 时间限制：1秒
# 空间限制：32768K
# 牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床
#
# 输入描述:
#
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
# 接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
# 接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
# 接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
# 数据保证至少有一个闹钟可以让牛牛及时到达教室。
#
# 输出描述:
#
# 输出两个整数表示牛牛最晚起床时间。
#
# 输入例子1:
#
# 3
# 5 0
# 6 0
# 7 0
# 59
# 6 59
#
# 输出例子1:
#
# 6 0


def can_go(clock, x, time):
    temp_1 = clock[0] + (x + clock[1]) // 60
    temp_2 = (x + clock[1]) % 60
    if temp_1 < time[0]:
        return True
    elif temp_1 == time[0]:
        if temp_2 <= time[1]:
            return True
        else:
            return False
    else:
        return False


n = int(input())
clock_list = []
for i in range(n):
    clock_list.append(list(map(int, input().split())))
for i in range(n):
    clock_list[i].append(clock_list[i][0] * 60 + clock_list[i][1])
clock_list.sort(key=lambda x: x[2])
x = int(input())
time = tuple(map(int, input().split()))
flag = 0
for i in range(n):
    if can_go(clock_list[i], x, time):
        flag = i
        continue
    else:
        break
print(str(clock_list[flag][0]) + ' ' + str(clock_list[flag][1]))
