def _transpose(matrix):
    res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res[i][j] = matrix[j][i]
    return res


def _matrix_multiply(matrix_left, matrix_right):
    [n_left, m_left] = [len(matrix_left), len(matrix_left[0])]
    [n_right, m_right] = [len(matrix_right), len(matrix_right[0])]
    res = [[0 for _ in range(m_right)] for _ in range(n_left)]
    for i in range(n_left):
        for j in range(m_right):
            for k in range(m_left):
                res[i][j] += matrix_left[i][k] * matrix_right[k][j]
    return res


def _mod(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] %= 1009
    return matrix


[n, m] = list(map(int, input().split()))
matrix_a = []
matrix_b = []
for _ in range(n):
    matrix_a.append(list(map(int, input().split())))
for _ in range(n):
    matrix_b.append(list(map(int, input().split())))
[n_c, m_c] = [n, m]
print(' '.join(list(map(str, [n_c, m_c]))))

# B * B^T * A

if n <= m:
    matrix_temp = _matrix_multiply(_transpose(matrix_b), matrix_a)
    ans = _mod(_matrix_multiply(matrix_b, matrix_temp))
    for i in range(n):
        print(' '.join(list(map(str, ans[i]))))
elif n > m:
    matrix_temp = _matrix_multiply(matrix_b ,_transpose(matrix_b))
    ans = _mod(_matrix_multiply(matrix_temp, matrix_a))
    for i in range(n):
        print(' '.join(list(map(str, ans[i]))))
