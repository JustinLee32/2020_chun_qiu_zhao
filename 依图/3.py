# def _check_in(point, interval):
#     if interval[0] <= point <= interval[1]:
#         return True
#     else:
#         return False


t = int(input())
whole_ans = []
for test_num in range(t):
    [n, m] = list(map(int, input().split()))
    points = list(map(int, input().split()))
    points.sort()
    ans = [0 for _ in range(n)]
    for _ in range(m):
        interval = list(map(int, input().split()))
        for i in range(n):
            if points[i] < interval[0]:
                continue
            elif points[i] >= interval[0]:
                if points[i] <= interval[1]:
                    ans[i] += 1
                else:
                    break
    # print("Case #%d:" % (test_num + 1))
    # for num in ans:
    #     print(num)
    whole_ans.append(ans)
for i in range(len(whole_ans)):
    print("Case #%d:" % (i + 1))
    for num in whole_ans[i]:
        print(num)









    # queen = []
    #
    # while points:
    #     temp_num = points.pop(0)
    #     while intervals and temp_num > intervals[0][1]:
    #         intervals.pop(0)
    #     while intervals and temp_num < intervals[0][0]:
    #         pass
    #     if not intervals:
    #         while queen and temp_num > queen[0][1]:
    #             queen.pop(0)
    #         else:
    #             print(len(queen))
    #     elif intervals:
    #         while intervals and intervals[0][1] >= temp_num:
    #             queen.append(intervals.pop(0))
    #         queen.sort(key=lambda x: x[1])
    #         print(len(queen))

