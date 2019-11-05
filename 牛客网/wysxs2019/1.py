# 0%
# 1/8
# [编程题]牛牛找工作
# 时间限制：2秒
# 空间限制：65536K
# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，
# 牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
#
# 输入描述:
#
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
# 接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
# 接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
# 保证不存在两项工作的报酬相同。
#
# 输出描述:
#
# 对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
#
# 输入例子1:
#
# 3 3
# 1 100
# 10 1000
# 1000000000 1001
# 9 10 1000000000
#
# 输出例子1:
#
# 100
# 1000
# 1001

[n, m] = list(map(int, input().split(" ")))
diff_salary_list = []
for i in range(n):
    diff_salary_list.append(tuple(map(int, input().split(" "))))
diff_salary_list.sort(key=lambda x: x[0])
member_list = list(map(int, input().split(" ")))
for member in member_list:
    res = 0
    flag = 0
    for i in range(len(diff_salary_list)):
        if member < diff_salary_list[i][0]:
            print(res)
            flag = 1
            break
        else:
            res = diff_salary_list[i][1]
            continue
    if not flag:
        print(diff_salary_list[-1][1])
