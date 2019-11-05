s=input();temp=[];a=""
temp.append(s)
for i in range(len(s)-1):
	a=s[0]
	s=s[1:]+a
	if s not in temp:
		temp.append(s)
print(len(temp))
