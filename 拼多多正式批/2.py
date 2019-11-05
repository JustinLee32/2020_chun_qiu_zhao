[n, m] = list(map(int, input().split()))
intervals = []
for _ in range(m):
    intervals.append(list(map(int, input().split())))
for i in range(m):
    intervals[i] = [intervals, i]
intervals.sort(key=lambda x: (x[0][0], x[0][1]))
trees = 0
end = -1
cache = []
for interval in intervals:
    if interval[0][1] <= end:
        print(trees)
        continue
    elif interval[1] > end:
        if interval[0] > end:
            trees += interval[1] - max(interval[0], end) + 1
        elif interval[0] <= end:
            trees += interval[1] - max(interval[0], end)
        end = interval[1]
        print(trees)
        continue
