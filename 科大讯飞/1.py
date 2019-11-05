day = int(input())
cache = [0 for _ in range(day)]


def _helper(day, temp1, temp2, maximum_day):
    global cache
    if day > maximum_day:
        return
    if day == 1:
        cache[day - 1] = 3
        _helper(day + 1, 0, 3, maximum_day)
    else:
        cache[day - 1] = temp1 + temp2
        _helper(day + 1, cache[day - 2], cache[day - 1], maximum_day)


_helper(0, 0, 0, day)
cache.reverse()


# def _recursion(day: int, today: int, cache: list) -> int:
#     if not day:
#         return today
#     return _recursion(day - 1, 2 * (today + cache[day - 1]), cache)

res = 0
for i in range(day):
    res = 2 * (res + cache[i])
print(res)
# print(_recursion(day, 0, cache))
