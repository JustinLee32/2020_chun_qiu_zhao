[n, s] = list(map(int, input().split()))
prices = list(map(int, input().split()))
res = len(prices)
if sum(prices) <= s:
    print(-1)
elif max(prices) > s:
    print(1)
else:
    left = 0
    right = 1
    total = prices[0]
    while total > s:
        total = prices[right]
        left += 1
        right += 1
    while right < len(prices):
        if total + prices[right] < s:
            total += prices[right]
            right += 1
        elif total + prices[right] >= s:
            if right > left:
                total -= prices[left]
                res = min(res, right-left+1)
                left += 1
            elif right == left:
                res = 1
                right += 1
    print(res)
