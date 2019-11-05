num = int(input())
sticks_list = list(map(int, input().split(" ")))
if num <= 2:
	print(-1)
else:
	flag = 0
	for i in range(3, num + 1):
		if 2 * max(sticks_list[:i]) < sum(sticks_list[:i]):
			flag = i
			break
		else:
			continue
	if flag:
		print(flag)
	else:
		print(-1)