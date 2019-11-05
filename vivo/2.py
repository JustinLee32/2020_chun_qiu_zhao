# '''
# Welcome to vivo !
# '''
def _delete(nums, temp):
    res = []
    for i in range(len(nums)):
        if i in temp:
            continue
        else:
            res.append(nums[i])
    return res



def solution(N, M):
    # TODO Write your code here
    ans = []
    nums = list(range(1, N+1))
    probe = 0
    flag = 1
    temp = []
    while nums:
        if not flag % M and flag > 0:
            flag = 1
            ans.append(nums[probe])
            temp.append(probe)
            probe += 1
        else:
            probe += 1
            flag += 1
        if probe == len(nums):
            probe = 0
            nums = _delete(nums, temp)
            temp = []
    print(' '.join(list(map(str, ans))))


N, M = [int(i) for i in input().split()]
solution(N, M)