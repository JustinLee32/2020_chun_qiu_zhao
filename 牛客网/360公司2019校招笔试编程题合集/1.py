num = int(input())
if num == 1:
	temp = list(map(int, input().split(" ")))
	print(max(temp) ** 2)
else:
	citizen_list = []
	for i in range(num):
		citizen_list.append(list(map(int, input().split(" "))))
	left_min = citizen_list[0][0]
	left_max = citizen_list[0][0]
	right_min = citizen_list[0][1]
	right_max = citizen_list[0][1]
	for i in range(num):
		if citizen_list[i][0] > left_max:
			left_max = citizen_list[i][0]
		if citizen_list[i][0] < left_min:
			left_min = citizen_list[i][0]
		if citizen_list[i][1] > right_max:
			right_max = citizen_list[i][1]
		if citizen_list[i][1] < right_min:
			right_min = citizen_list[i][1]
	ans = max(left_max - left_min, right_max - right_min) ** 2
	print(ans)