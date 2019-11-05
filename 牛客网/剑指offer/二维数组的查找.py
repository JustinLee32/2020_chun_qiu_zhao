# 时间限制：1秒 空间限制：32768K 热度指数：1277943
# 本题知识点： 查找 数组
# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        n = len(array[0])
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if target > array[i][j]:
                j += 1
                continue
            elif target < array[i][j]:
                i -= 1
                continue
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # print(sol.Find(target, array))
