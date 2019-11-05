# 多源D点
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 给出一棵n个结点的树，树上每条边的边权都是1，这n个结点中有m个特殊点，请你求出树上距离这m个特殊点距离均不超过d的点的数量，包含特殊点本身。
#
# 输入
# 输入第一行包含三个正整数，n,m,d分别表示树上有n个结点，其中有m个点是特殊点，d是如题所示的距离。（1<=n,m,d<=50000）
#
# 第二行m个整数，表示特殊的点的编号，编号在1-n之间。
#
# 第三行有n-1个整数，第i个数表示第i+1号结点的父亲结点的编号，同样在1-n之间。
#
# 输出
# 输出仅包含一个整数，即符合题目要求的点的数量。
#
#
# 样例输入
# 6 2 3
# 2 1
# 3 4 5 6 1
# 样例输出
# 2


[n, m, d] = list(map(int, input().split()))
m_list = list(map(int, input().split()))
father_list = list(map(int, input().split()))
node_dic = {}
for i in range(n):
    node_dic[i+1] = []
for i, num in enumerate(father_list):
    node_dic[num].append(i+2)
for i, num in enumerate(father_list):
    node_dic[i+2].append(num)
res_temp = []
for node in m_list:
    visted = [node]
    temp = []
    for i in range(d):
        t = node_dic[node]
        for num in t:
            if num in visted:
                continue
            else:
                o = num
                visted.append(o)
        temp.append(node_dic[o])
for myset in temp_list:
	res_set = res_set & myset
print(len(res_set))

