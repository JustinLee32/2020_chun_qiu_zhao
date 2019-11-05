# 3/8
# [编程题]字符串碎片
# 时间限制：1秒
# 空间限制：32768K
# 一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少。
#
# 输入描述:
#
# 输入包括一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),s只含小写字母('a'-'z')
#
# 输出描述:
#
# 输出一个整数,表示所有碎片的平均长度,四舍五入保留两位小数。
#
# 如样例所示: s = "aaabbaaac"
# 所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25
#
# 输入例子1:
#
# aaabbaaac
#
# 输出例子1:
#
# 2.25

string = input()
temp_list = []
temp = 1
if len(string) == 1:
    print('%.2f' % 1)
else:
    i = 0
    j = 1
    while j < len(string):
        if string[i] == string[j]:
            j += 1
            temp += 1
        elif string[i] != string[j]:
            temp_list.append(temp)
            temp = 1
            i = j
            j += 1
    temp_list.append(temp)
    print('%.2f' % (sum(temp_list) / len(temp_list)))