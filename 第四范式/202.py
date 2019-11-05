from time import time
t1 = time()
n = 3142213424324
s = str(n)
t2 = time()
add = n
flag = 0
def calsum(s):
	add = 0
	for i in range(len(s)):
		add+=int(s[i])**2
	if add==1:
		return -1
	else:
		return add
while add>=0:
	add = calsum(str(add))
	t2 = time()
	if float(t2 - t1) > 0.1:
		flag = 1
		break
if flag==0:
	print("True")
else:
	print("False")
	