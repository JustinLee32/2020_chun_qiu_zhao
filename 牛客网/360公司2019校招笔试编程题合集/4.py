[n, m] = list(map(int, input().split(" ")))
a_list = list(map(int, input().split(" ")))
q = int(input())
for i in range(q):
	[l, r] = list(map(int, input().split(" ")))
	print(len(set(a_list[l - 1:r])))
	