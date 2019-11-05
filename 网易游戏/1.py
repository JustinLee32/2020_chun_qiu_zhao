n = int(input())
# 用户名，贴吧名
# 贴吧名， 用户名
dic_1 = {}
dic_2 = {}
for i in range(n):
    temp = list(map(str, input().split()))
    if temp[1] not in dic_1:
        dic_1[temp[1]] = [temp[0]]
    else:
        dic_1[temp[1]] += [temp[0]]
    if temp[0] not in dic_2:
        dic_2[temp[0]] = [temp[1]]
    else:
        dic_2[temp[0]] += [temp[1]]
temp = {}
temp_list = []
for key, value in dic_2.items():
    if len(value) > 2:
        temp[key] = set(value)
        temp_list.append(key)
    else:
        continue
temp_list.sort()
for i in range(len(temp_list)):
    for j in range(len(temp_list)):
        if j == i:
            continue
        else:
            res = []
            res.append(temp_list[i])
            res.append(temp_list[j])
            res.append(str(len(temp[temp_list[i]] & temp[temp_list[j]])))
            print(' '.join(res))
