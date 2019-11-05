grid = [[1,1,0,0,0],
		[1,1,0,0,0],
		[0,0,1,0,0],
		[0,0,0,1,1]]
if not grid:
	print(0)
m = len(grid); n = len(grid[0]); count = 0
ans = 0
for i in range(m):
	for j in range(n):
		if grid[i][j] > 0:
			count+=1
stack=[]
def getnext(grid):
	for i in range(m):
		for j in range(n):
			if grid[i][j] > 0:
				return [i,j]
def getneighbors(i,j):
	res = []
	if i > 0:
		if grid[i-1][j] > 0:
			res.append([i-1,j])
	if i < m-1:
		if grid[i+1][j] > 0:
			res.append([i+1,j])
	if j > 0:
		if grid[i][j-1] > 0:
			res.append([i,j-1])
	if j < n-1:
		if grid[i][j+1]>0:
			res.append([i,j+1])
	return res

while count:
	while stack:
		[i,j] = stack.pop()
		neighbors = getneighbors(i,j)
		for neighbor in neighbors:
			stack.append(neighbor)
			grid[neighbor[0]][neighbor[1]] = 0
			count-=1
	if count:
		[i,j] = getnext(grid)
		stack.append([i,j])
		grid[i][j] = 0
		count-=1
		ans+=1
print(ans)
		
