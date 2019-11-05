strlist = input()
strlist=strlist.split()
def cutstr(string):
	temp=[];p=len(string);n=p//8;m=8-p%8;
	if m<8:
		n+=1
	if m>0:
		for i in range(m):
			string+="0"
	if n==0:
		temp.append(string)
	else:
		for i in range(n):
			temp.append(string[8*i:8*(i+1)])
	return temp
newstrlist=[]       
for i in range(1,int(strlist[0])+1):
	newstrlist.extend(cutstr(strlist[i]))
	
newstrlist.sort()
for strs in newstrlist:
	print(strs,end=" ")
