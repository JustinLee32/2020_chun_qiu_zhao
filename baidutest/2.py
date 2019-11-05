a=input()
b=input()
q=input()
mya=""
for i in range(int(q)):
	flag=0
	s=input()
	x=s.split(" ")
	for i in range(len(x)):
		x[i]=int(x[i])
	mya=a[x[0]-1:x[1]]
	for i in range(len(mya)-len(b)+1):
		if mya[i:i+len(b)]==b:
			flag+=1
	print(flag)