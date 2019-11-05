import sys


def dfs(vertex, inverse_adj, visited):
    if visited[vertex] == 2:
        return True
    if visited[vertex] == 1:
        return False

    visited[vertex] = 2
    for precursor in inverse_adj[vertex]:
        if dfs(precursor, inverse_adj, visited):
            return True

    visited[vertex] = 1
    return False


for line in sys.stdin:
    G = eval(line)
    res = 0
    visited = [0 for _ in range(len(G))]
    inverse_adj = [set() for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]:
                inverse_adj[j].add(i)
            else:
                continue
    for i in range(len(G)):
        if dfs(i, inverse_adj, visited):
            res = 1
            break
    print(res)



