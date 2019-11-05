# 时间限制：1秒 空间限制：32768K 热度指数：983128
# 本题知识点： 链表
# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        probe = listNode
        res = []
        while probe:
            res.append(probe.val)
            probe = probe.next
        return res[::-1]


if __name__ == '__main__':
    node = ListNode([1, 2, 3])
    sol = Solution()
    print(sol.printListFromTailToHead(node))
