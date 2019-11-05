A = list(map(int, input().split(' ')))
m = A[0]
n = A[1]
k = A[2]

matrix = []
for i in range(m):
    for j in range(n):
        matrix.append((i+1)*(j+1))
matrix.sort()
print(matrix[-k])
