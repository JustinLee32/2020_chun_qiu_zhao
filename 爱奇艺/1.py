def find_repeat(string: str) -> int:
    res = 0
    for i in range(len(string)-1):
        temp = len(string) - 1 - i
        if string[:i+1] == string[temp:]:
            res = i + 1
        else:
            continue
    return min(res, len(string)-1)


def check(s, t, start, end) -> bool:
    if end - start < len(t):
        return False
    return True if t in s[start:end+1] else False


s = input()
t = input()
repeat = find_repeat(t)
ans = ""
cache = 0
for i in range(len(t)):
    ans += '0 '
start = 0
for i in range(len(t)-1, len(s), 1):
    end = i
    if check(s, t, start, end):
        cache = cache + 1
        if repeat:
            start = end - repeat + 1
        else:
            start = end + 1
        ans += str(cache) + ' '
    else:
        ans += str(cache) + ' '
        continue
print(ans.strip())
