def _can_win(x, y):
    interval = [abs(x - y), abs(x + y)]
    interval.sort()
    if interval[0] <= abs(x) and interval[1] >= abs(y):
        return True
    else:
        return False


n = int(input())
points = list(map(int, input().split()))
ans = 0
points.sort()
for i in range(len(points)-1):
    [left, right] = sorted([abs(points[i]), abs(points[-1])])
    if _can_win(left, right):
        ans += (len(points) - i - 1)
print(ans)
