def move(probe, s, res: list) -> list:
    if s[probe] == 'R':
        for i in range(probe, len(s)):
            if s[i] == 'L':
                flag = i
                break
            else:
                continue
        cha = abs(flag - probe)
        if cha % 2:
            res[flag-1] += 1
        else:
            res[flag] += 1
    elif s[probe] == 'L':
        for i in range(probe, -1, -1):
            if s[i] == 'R':
                flag = i
                break
            else:
                continue
        cha = abs(flag - probe)
        if cha % 2:
            res[flag+1] += 1
        else:
            res[flag] += 1
    return res


s = input()
res = [0 for i in range(len(s))]
for i in range(len(s)):
    res = move(i, s, res)
print(' '.join(list(map(str, res))))
