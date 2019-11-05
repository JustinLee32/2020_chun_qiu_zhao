def check(s: str, num: str, size: int) -> bool:
    for i in range(size):
        if s[i] == '?':
            continue
        else:
            if s[i] == num[i]:
                continue
            else:
                return False
    return True


def decorate(num: str, size: int) -> bool:
    if len(num) < size:
        num = '0' * (size - len(num)) + num
    return num


s = input()
size = len(s)
res = 0
for num in range(5, 10**size, 13):
    if check(s, decorate(str(num), size), size):
        res += 1
    else:
        continue
print(res % (10 ** 9 + 7))
