n = int(input())
map_dic = {}
start_list = []
end_list = []
res_dic = {}
temp_num = 0
res_list = []
res = []
for i in range(n):
    temp = list(map(int, input().split()))
    start_list.append(temp[0])
    end_list.append(temp[1])
for i in range(n):
    map_dic[end_list[i]] = start_list[i]
for i in range(n):
    res_dic[start_list[i]] = 0
    res_dic[end_list[i]] = 0
for i in range(len(start_list)):
    num = start_list[i]
    res_dic[num] += 1
    while num in map_dic:
        num = map_dic[num]
        res_dic[num] += 1
for key, value in res_dic.items():
    res_list.append((key, value))
res_list.sort(key=lambda x: x[1], reverse=True)
dianji = res_list[0][1]
for i in range(len(res_list)):
    if res_list[i][1] == dianji:
        res.append(res_list[i])
    else:
        break
res.sort(key=lambda x: x[0], reverse=True)
print(res[0][0])
