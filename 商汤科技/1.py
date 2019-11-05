m = int(input())
ans = 0
if m == 0:
    print(1)
else:
    while m > 1:
        ans += 1
        if not m % 3:
            m = m / 3
            continue
        elif m % 3 == 1:
            m = m + 1
            continue
        elif not m % 2:
            m = m / 2
            continue
        else:
            m += 1
            continue
    print(ans)
