n=int(input());nums=[]
nums=list(map(int,input().split()))
w=0;step=0
left=0;right=1;flag=0
while right<=n-1:
	if nums[left]>=nums[right]:
		if flag==1:
			step+=2;w=w+nums[right-1]-nums[left]
		left=right;right=right+1;flag=0
	else:
		right+=1;flag=1
if flag==1:
	step+=2;w+=nums[-1]-nums[left]
print(w,step)