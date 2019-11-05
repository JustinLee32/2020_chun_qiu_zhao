n=int(raw_input());mylist=[]
for i in range(n):
	mylist.append(float(raw_input().strip(" ")))
ming=0;hua=0;flag=0;flag1=0;flag2=0;flag3=0
while ming+hua<=1 and flag3<=99:
	flag2=0#ming get
	if flag>=n:
		flag-=n;flag1+=1
	if flag%2==0 and flag1%2==0:
		ming+=mylist[flag];flag+=1;flag3+=1
	elif flag%2==1 and flag1%2==0:
		hua+=mylist[flag];flag+=1;flag2=1;flag3+=1
	elif flag%2==0 and flag1%2==1:
		hua+=mylist[flag];flag+=1;flag2=1;flag3+=1
	elif flag%2==1 and flag1%2==1:
		ming+=mylist[flag];flag+=1;flag3+=1
if flag2==0:
	ming-=mylist[flag];ming=1-hua
print("%.4f" %round(ming,4))