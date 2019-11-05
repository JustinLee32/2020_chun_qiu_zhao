n=int(input());nums=[]
for i in range(n):
	nums.append(list(map(int,input().split())))

def isover(hezi,qiu,zong):
	if hezi**qiu>=zong:
		return 1
	else:
		return 0
		
for i in range(n):
	step=1;flag=0;hezi=nums[i][0];qiu=nums[i][1];zong=nums[i][2]
	if nums[i][0]==1:
		print("A&B")
		continue
	while flag==0:
		temp1=(hezi+1)**qiu;temp2=hezi**(qiu+1)
		if temp1<=temp2:
			hezi+=1
			flag=isover(hezi,qiu,zong)
		else:
			qiu+=1
			flag=isover(hezi,qiu,zong)
		step+=1
	if step%2==1:
		print("B")
	else:
		print("A")
