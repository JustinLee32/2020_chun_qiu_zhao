def select(now, step, total):
    if now - step - 1 > total - now - step:
        # 离1远，往正方向走
        return 0
    elif now - step - 1 <= total - now - step:
        # 离1近，往负方向走
        return 1


def is_ok(first, n, steps):
    now = first
    for step in steps:
        if now - step < 1:
            if now + step > n:
                return False
            elif now + step < n:
                now += step
                continue
        elif now - step > 1:
            if now + step > n:
                now -= step
                continue
            elif now + step < n:
                flag = select(now, step, n)
                if flag:
                    now -= step
                elif not flag:
                    now += step
    return True


[n, m] = list(map(int, input().split()))
steps = []
res = 0
for i in range(m):
    steps.append(int(input()))
steps.reverse()
for i in range(1, n+1):
    if is_ok(i, n, steps):
        res += 1
print(res)


