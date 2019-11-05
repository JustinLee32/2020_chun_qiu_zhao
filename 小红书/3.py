# 有N件衣服，每件衣服有指定的价格P和价值V（代表小红薯的喜欢程度）
#
# 每件候选衣服只能买一件，预算B限定了总价格上限，衣橱空间S限定了总件数上限
#
# 希望选择合适的衣服组合，使总价值尽量大
#
# 当有多个方案总价值相同时，希望总价格尽量小，总价格也相同时，希望购买件数尽量少


[n, b, s] = list(map(int, input().split()))
prices = []
values = []
for i in range(n):
    temp = list(map(int, input().split(' ')))
    prices.append(temp[0])
    values.append(temp[1])
prices_values = list(zip(prices, values))
prices_values.sort(key=lambda x: x[0])
dp = [[0 for _ in range(b)] for _ in range(s)]
probe = 0
flag = 0
xiaofei = [0 for i in range(b)]
# temp_value = 0
for j in range(b):
    while j >= prices_values[probe][0]:
        flag = 1
        # temp_value += prices_values[probe][1]
        probe += 1
    if not flag:
        dp[0][j] = 0
    else:
        dp[0][j] = prices_values[probe-1][1]
for j in range(1, b):
    if dp[j] > dp[j-1]:
        xiaofei[j] = xiaofei[j-1] + 1
    else:
        xiaofei[j] = xiaofei[j-1]
for i in range(1, s-1):
    for j in range(b):
        dp[i][j] = max([dp[i-1][k] + dp[0][j-k] for k in range(j+1)])
max = dp[-1][-1]
[total_price, total_num] = [1, 1]
for j in range(b-1, -1, -1):
    if dp[-1][j] == max:
        continue
    else:
        total_price = j + 1
        break
for i in range(s-1, -1, -1):
    if dp[i][total_price] == max:
        continue
    else:
        total_num = i + 1
        break
res = [max, total_price, total_num]
print(' '.join(list(map(str, res))))

