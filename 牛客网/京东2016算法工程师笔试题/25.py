# 25/25
# [编程题]小球的距离
# 时间限制：3秒
# 空间限制：32768K
# 小东和三个朋友一起在楼上抛小球，他们站在楼房的不同层，假设小东站的楼层距离地面N米，球从他手里自由落下，
# 每次落地后反跳回上次下落高度的一半，并以此类推直到全部落到地面不跳，求4个小球一共经过了多少米？(数字都为整数)
# 给定四个整数A,B,C,D，请返回所求结果。
# 测试样例：
# 100,90,80,70
# 返回：1020


# -*- coding:utf-8 -*-

class Balls:
    def calcDistance(self, A, B, C, D):
        return 3 * (A + B + C + D)


if __name__ == '__main__':
    [A, B, C, D] = list(map(int, input().split(",")))
    ball = Balls()
    print(ball.calcDistance(A, B, C, D))
