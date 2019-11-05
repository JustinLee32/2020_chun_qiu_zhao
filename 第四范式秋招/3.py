# 给定一个由0和1组成的数组A，我们可以最多将其中K个0变为1，返回该数组中只包含1的最长连续子数组的长度，并给出算法的时间、空间复杂度。
#
#
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
#
# 输出：6


# coding=utf-8
import sys

a = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

# O(N)
left = 0
right = 0
record = []
while right < len(a):
    if not a[left]:
        a[left] += 1
        a[right] += 1
    elif a[left] == 1:
        if a[right]:
            right += 1
        else:
            record.append([left, right])
            left = right
if a[right - 1] == 1:
    record.append([left, right])


def _add_one(queue, k):
    if len(queue) == 1:
        return queue[0][1] - queue[0][0] + 1 + k
    else:
        temp = 0
        for i in range(len(queue) - 1):
            temp += queue[i + 1][0] - temp[i][1] - 1
            if temp > k:
                return -1
        return queue[-1][1] - queue[0][0] + 1 + (k - temp)


ans = 0
queue = []
while record or queue:
    queue.append(record.pop(0))
    cache = _add_one(queue, k)
    if cahce >= 0:
        ans = max(ans, min(len(a), _add_one(queue, k)))
    elif cache == -1:
        queue.pop(0)

print(ans)
