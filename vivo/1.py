# '''
#  Welcome to vivo !
# '''

def can_jump(step_list):
    start = 0
    end = 0
    n = len(step_list)
    while start <= end and end < len(step_list) - 1:
        end = max(end, step_list[start] + start)
        start += 1
    return end >= n - 1


def solution(step_list):

    # // TODO Write your code here

    if not can_jump(step_list):
        return -1
    if len(step_list) == 1:
        return 0
    else:
        # n = len(step_list)
        # dp = [float("inf") for _ in range(n)]
        # dp[0] = 0
        # for i in range(1, len(step_list)):
        #     for j in range(i):
        #         if step_list[i] >= i - j:
        #            dp[i] = min(dp[i], dp[j] + 1)
        # return int(dp[-1])
        steps, start, end, far = 0, 0, 0, 0
        while end < len(step_list) - 1:
            steps += 1
            for i in range(start, end+1):
                far = max(far, step_list[i] + 1)
            start, end = end + 1, far
        return steps


step_list = [int(i) for i in input().split()]
print(solution(step_list))
