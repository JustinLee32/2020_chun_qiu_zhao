# 每位骑手拿出装有货物的保温箱，参赛选手需在最短的时间内用最少的保温箱将货物装好。
# 我们把问题简单描述一下:
# 1.每个货物占用空间都一模一样
# 2.外卖小哥保温箱的最大容量是不一样的, 每个保温箱由两个值描述: 保温箱的最大容量bi, 当前已有货物个数ai, (ai <= bi)
# 3.货物转移的时候, 不必一次性全部转移, 每转移一件货物需要花费1秒的时间

# 输入
# 第一行包含 一个整数 n，(1<=n<=100) 表示保温箱的数量
# 第二行有 n 个正整数 a1,a2,…,an(1<=ai<=100)
# ai表示第 i个保温箱的已有货物个数
# 第三行有 n 个正整数 b1,b2,…,bn(1<=bi<=100),bi 表示第 i 个保温箱的最大容量
# 显然,每一个ai<=bi

# 输出
# 输出为两个整数 k 和 t, k 表示能容纳所有货物的保温箱的最少个数,t 表示将所有货物转移到这 k 个保温箱所花费的最少时间,单位为秒.



time= 0
num = 0
n = int(input())
initial = list(map(int, input().split()))
total = sum(initial)
volume = list(map(int, input().split()))
cha = []
for i in range(n):
    cha.append(volume[i]-initial[i])
zhuangtai = list(zip(volume, initial, cha))
zhuangtai.sort(key=lambda x: x[2], reverse=True)
temp = 0
flag = -1
for i in range(len(zhuangtai)):
    temp += zhuangtai[i][0]
    if temp >= total:
        flag = i
        break
    else:
        continue
if flag == -1:
    print(' '.join([str(n), str(time)]))
else:
    if flag == n-1:
        print(' '.join([str(flag+1), str(0)]))
    for i in range(flag+1, n):
        time += zhuangtai[i][1]
    print(' '.join([str(flag+1), str(time)]))
