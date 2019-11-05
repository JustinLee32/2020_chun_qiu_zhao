a=[1,2,1,2,1];dp=[]
for i in range(len(a)):
	dp.append(0)
dp[0]=0
for i in range(1,len(a)):
	if a[i-1]>1:
		dp[i] = dp[i-1]
	else:
		dp[i] = abs(dp[i-1]-1)
if dp[len(a)-1]==0:
	print("Alice")
else:
	print("Bob")