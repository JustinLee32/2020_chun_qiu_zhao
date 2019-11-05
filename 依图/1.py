t = int(input())
for num_test in range(t):
    [n, m, a, b, c] = list(map(int, input().split()))
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    matrix[a][b] = c
    for i in range(n):
        for j in range(m):
            cha = abs(i-a) + abs(j-b)
            matrix[i][j] = max(0, c - cha)
    print("Case #%d:" % (num_test+1))
    for i in range(n):
        print(' '.join(list(map(str, matrix[i]))))
