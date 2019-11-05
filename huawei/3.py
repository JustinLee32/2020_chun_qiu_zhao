size=list(map(int,input().split())) #size of matrix
a=list(map(int,input().split())) #position of a
b=list(map(int,input().split())) #position of b
matrix=[]
for i in range(size[0]):
	matrix.append(list(map(int,input().split())))

global ans
ans=0

temp=[];temp1=[];temp.append(matrix[a[0]][a[1]]);temp1.append([a[0],a[1]])
def getnext(matrix,i,j,temp,temp1,size):
	print(temp,temp1)
	if i==0:
		if j==0:
			if matrix[i][j+1]>matrix[i][j]:
				temp.append(matrix[i][j+1]);temp1.append([i,j+1])
			if matrix[i+1][j]>matrix[i][j]:
				temp.append(matrix[i+1][j]);temp1.append([i+1,j])
		elif j==size[1]-1:
			if matrix[i][j-1]>matrix[i][j]:
				temp.append(matrix[i][j-1]);temp1.append([i,j-1])
			if matrix[i+1][j]>matrix[i][j]:
				temp.append(matrix[i+1][j]);temp1.append([i+1,j])
		else:
			if matrix[i][j-1]>matrix[i][j]:
				temp.append(matrix[i][j-1]);temp1.append([i,j-1])
			if matrix[i][j+1]>matrix[i][j]:
				temp.append(matrix[i][j+1]);temp1.append([i,j+1])
			if matrix[i+1][j]>matrix[i][j]:
				temp.append(matrix[i+1][j]);temp1.append([i+1,j])
	elif i==size[0]-1:
		if j==0:
			if matrix[i][j+1]>matrix[i][j]:
				temp.append(matrix[i][j+1]);temp1.append([i,j+1])
			if matrix[i-1][j]>matrix[i][j]:
				temp.append(matrix[i-1][j]);temp1.append([i-1,j])
		elif j==size[1]-1:
			if matrix[i][j-1]>matrix[i][j]:
				temp.append(matrix[i][j-1]);temp1.append([i,j-1])
			if matrix[i-1][j]>matrix[i][j]:
				temp.append(matrix[i-11][j]);temp1.append([i-1,j])
		else:
			if matrix[i][j-1]>matrix[i][j]:
				temp.append(matrix[i][j-1]);temp1.append([i,j-1])
			if matrix[i][j+1]>matrix[i][j]:
				temp.append(matrix[i][j+1]);temp1.append([i,j+1])
			if matrix[i-1][j]>matrix[i][j]:
				temp.append(matrix[i-1][j]);temp1.append([i-1,j])
	elif j==0 or j==size[1]-1:
		if matrix[i+1][j]>matrix[i][j]:
			temp.append(matrix[i+1][j]);temp1.append([i+1,j])
		if matrix[i-1][j]>matrix[i][j]:
			temp.append(matrix[i-1][j]);temp1.append([i-1,j])
		if j==0:
			if matrix[i][j+1]>matrix[i][j]:
				temp.append(matrix[i][j+1]);temp1.append([i,j+1])
		if j==size[1]-1:
			if matrix[i][j-1]>matrix[i][j]:
				temp.append(matrix[i][j-1]);temp1.append([i,j-1])			
	else:
		if matrix[i+1][j]>matrix[i][j]:
			temp.append(matrix[i+1][j]);temp1.append([i+1,j])
		if matrix[i-1][j]>matrix[i][j]:
			temp.append(matrix[i-1][j]);temp1.append([i-1,j])
		if matrix[i][j-1]>matrix[i][j]:
			temp.append(matrix[i][j-1]);temp1.append([i,j-1])
		if matrix[i][j+1]>matrix[i][j]:
			temp.append(matrix[i][j+1]);temp1.append([i,j+1])
	return temp,temp1
	
def climb(matrix,temp,temp1,size,ans):
	print(temp,temp1);print(ans)
	if temp:
		temp.pop()
		[i,j]=temp1.pop()
		if i==b[0] and j==b[1]:
			ans+=1
			temp,temp1=getnext(matrix,i,j,temp,temp1,size)
			climb(matrix,temp,temp1,size,ans)
		else:
			temp,temp1=getnext(matrix,i,j,temp,temp1,size)
			climb(matrix,temp,temp1,size,ans)	
	else:
		#print(ans)
		print("!!")
		return ans

#climb(matrix,temp,temp1,size,ans)
res=climb(matrix,temp,temp1,size,ans)
print(res)
