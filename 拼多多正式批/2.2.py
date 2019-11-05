def _plant_trees(planted: set, interval: list):
    res = 0
    to_plant = set(list(range(interval[0], interval[1] + 1)))
    need_to_plant = to_plant - planted
    planted = planted | need_to_plant
    return len(need_to_plant), planted


[n, m] = list(map(int, input().split()))
intervals = []
for _ in range(m):
    intervals.append(list(map(int, input().split())))
trees = 0
planted = set()
for interval in intervals:
    temp, planted = _plant_trees(planted, interval)
    trees += temp
    print(trees)
