# 4/8
# [编程题]游历魔法王国
# 时间限制：1秒
# 空间限制：32768K
# 魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
# 小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
# 如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。
#
# 输入描述:
#
# 输入包括两行,第一行包括两个正整数n(2 ≤ n ≤ 50)和L(1 ≤ L ≤ 100),表示城市个数和小易能行动的次数。
# 第二行包括n-1个整数parent[i](0 ≤ parent[i] ≤ i), 对于每个合法的i(0 ≤ i ≤ n - 2),在(i+1)号城市和parent[i]间有一条道路连接。
#
# 输出描述:
#
# 输出一个整数,表示小易最多能游历的城市数量。
#
# 输入例子1:
#
# 5 2
# 0 1 2 3
#
# 输出例子1:
#
# 3

list_1 = list(map(int, input().split(" ")))
[n, l] = list_1
list_2 = list(map(int, input().split(" ")))
city_dic = {}
for i in range(1, n):
    city_dic[i] = list_2[i-1]
city_dic[0] = 0
ans = 0
for key, value in city_dic.items():
    temp_list = []
    mark = key
    temp_list.append(mark)
    for j in range(l):
        temp_list.append(city_dic[mark])
        mark = city_dic[mark]
    temp_num = len(set(temp_list))
    if temp_num > ans:
        ans = temp_num
    if ans == n:
        break
print(ans)
