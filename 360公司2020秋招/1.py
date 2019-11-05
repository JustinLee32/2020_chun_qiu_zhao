# 寻找子串
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 英语老师看你老是在英语课上和周围同学交头接耳，所以给你布置了一份额外的家庭作业来惩罚惩罚你：你有一个字符串s，请你在s的所有子串中，找到出现次数最多的子串，告诉老师它的出现次数。
#
# 输入
# 共一行，一个字符串s，仅由英文小写字母组成，1≤|s|≤10000。
#
# 输出
# 一个正整数，表示最大出现次数。
#
#
# 样例输入
# aba
# 样例输出
# 2
#
# 提示
# aba的所有子串为a、b、a、ab、ba、aba，其中a的出现次数最多，出现了2次。

s = input()
if len(s) <= 1:
    print(s)
dic = {}
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1
res = 0
for key, value in dic.items():
    res = max(res, value)
print(res)
