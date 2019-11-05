n = int(input())
a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))
temp1 = []
temp2 = []
ans = 0
for i in range(1, n):
	if a_list[i] > a_list[i-1]:
		temp1.append(1)
	else:
		temp1.append(-1)
	if b_list[i] > b_list[i-1]:
		temp2.append(1)
	else:
		temp2.append(-1)
for i in range(n-1):
	if temp1[i] == -1 and temp2[i] == -1:
		pass
	else:
		ans += 1
print(ans + 1)