def if_sum_n_distinct_fib(x, n):
	def fib(n):
		if n == 0:
			return 1
		if n == 1:
			return 1
		return fib(n-1) + fib(n-2)
	temp=[];temp1=0;k=1
	while temp1<x:
		temp1=fib(k)
		k+=1;temp.append(temp1)
	print(temp,x,n)
	if n==0 and x==0:
		return 1
	elif n==0 and x!=0:
		return 0
	elif x==0 and n!=0:
		return 0
	else:
		for i in range(len(temp)):
			if if_sum_n_distinct_fib(x-temp[i],n-1):
				return True
			else:
				continue
		return False

print(if_sum_n_distinct_fib(5,3))