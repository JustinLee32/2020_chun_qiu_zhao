string = input()
def copystr(num,mystr):
	temp=""
	for i in range(num):
		temp+=mystr
	return temp

def mycopy(string,num):
	left=0;right=0;flag=0
	for i in range(len(string)):
		if string[i]=="(":
			left+=1
			flag=1
		if string[i]==")":
			right+=1
		if flag==1 and left==right:
			break
	if flag==0:
		return copystr(num,string)
	else:
		a=string.index("(");
		mynum=""
		for j in range(a-1,-1,-1):
			if string[j]<="9" and string[j]>="0":
				mynum+=string[j]
			else:
				break
		l=len(mynum)
		mynum=int(mynum[::-1])
		string=string[:a-l]+mycopy(string[a+1:i],int(mynum))+string[i+1:]
		string=copystr(num,string)
	return string
string=mycopy(string,1)
print(string[::-1])