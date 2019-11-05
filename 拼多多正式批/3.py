[n, m, k] = list(map(int, input().split()))
jishu = 0
ans = []


def _recursion(k, visted, num_a, num_b):
    global jishu, ans
    if jishu == k:
        ans.extend(visted)
        return
    elif jishu <= k:
        if num_a < n:
            jishu += 1
            _recursion(k, visted + ['a'], num_a + 1, num_b)
        if num_b < m:
            jishu += 1
            _recursion(k, visted + ['b'], num_a, num_b + 1)


_recursion(k, [], 0, 0)
print(''.join(ans))
