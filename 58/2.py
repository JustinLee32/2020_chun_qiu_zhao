def calc_sum(cache):
    ans = 0
    now = 0
    num = 0
    for i in range(len(cache)-1, -1, -1):
       if not now:
            num += 1
            ans += num
            now = cache[i]
       else:
           if cache[i] > now:
               num += 1
               ans += num
           elif cache[i] == now:
               ans += num
    return ans


n = int(input())
scores = []
res = 0
for i in range(n):
    scores.append(int(input()))
cache = []
if n <= 1:
    print(1)
else:
    for i in range(n):
        if not cache:
            cache.append(scores[i])
        elif scores[i] <= cache[-1]:
            cache.append(scores[i])
        elif scores[i] > cache[-1]:
            res += calc_sum(cache)
            cache = []
            cache.append(scores[i])
print(res)
