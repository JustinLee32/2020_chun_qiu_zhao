s = input()
if not s:
    print(0)
else:
    [left, res] = [0, 0]
    for i in range(len(s)):
        if s[i] == ']':
            if not left:
                res += 1
            else:
                left -= 1
        elif s[i] == '[':
            left += 1
    if left:
        res += left
    print(res)
