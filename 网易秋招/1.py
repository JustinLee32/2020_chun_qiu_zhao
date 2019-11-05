def _eat_grape(grape, ans, residue):
    if grape[1] == 1:
        if grape[0] % 2:
            ans[0] += grape[0] // 2
            ans[2] += grape[0] // 2
            residue[0] += 1
        else:
            ans[0] += grape[0] // 2
            ans[2] += grape[0] // 2
    elif grape[1] == 2:
        if grape[0] % 2:
            ans[0] += grape[0] // 2
            ans[1] += grape[0] // 2
            residue[1] += 1
        else:
            ans[0] += grape[0] // 2
            ans[1] += grape[0] // 2
    elif grape[1] == 3:
        if grape[0] % 2:
            ans[1] += grape[0] // 2
            ans[2] += grape[0] // 2
            residue[2] += 1
        else:
            ans[1] += grape[0] // 2
            ans[2] += grape[0] // 2
    return ans, residue


t = int(input())
for _ in range(t):
    ans = [0 for _ in range(3)]
    residue = [0 for _ in range(3)]
    grapes = list(map(int, input().split()))
    grapes = list(zip(grapes, [1, 2, 3]))
    grapes.sort(key=lambda x: -x[0])
    for _ in range(3):
        grape = grapes.pop(0)
        ans, residue = _eat_grape(grape, ans, residue)
    if residue[0]:
        if ans[0] < ans[2]:
            ans[0] += 1
        else:
            ans[2] += 1
    if residue[1]:
        if ans[0] < ans[1]:
            ans[0] += 1
        else:
            ans[1] += 1
    if residue[2]:
        if ans[1] < ans[2]:
            ans[1] += 1
        else:
            ans[2] += 1
    print(max(ans))
