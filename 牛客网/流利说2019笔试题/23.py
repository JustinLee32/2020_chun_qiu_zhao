num = int(input())
nums_list = []
if num == 1:
	print(input())
else:
	for i in range(num):
		nums_list.append(int(input()))
	sum_list = []
	for i in range(num + 1):
		sum_list.append(sum(nums_list[:i]))
	print(max(sum_list) - min(sum_list))