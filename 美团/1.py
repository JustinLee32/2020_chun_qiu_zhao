#!/bin/python
# -*- coding: utf8 -*-


def findMaxSubListLen(a, b):
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = dp[i+1][j+1] + 1
    temp = 0
    [first, second] = [0, 0]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if dp[i][j] > temp:
                temp = dp[i][j]
                first = i
                second = j
            else:
                continue
    # return a[first-temp:first]
    return temp
# ******************************结束写代码******************************


len_a = int(input())
a = list(input().split())
len_b = int(input())
b = list(input().split())
print(findMaxSubListLen(a, b))
