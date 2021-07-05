#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 4:18 下午
# @Site    : 
# @File    : no62.py
# @desc    :
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 构造矩阵，由于只能向左和向下移动，f[0][0]->f[m][0]和f[0][0]->f[0][n]均只有1种走法
        f = list()
        f_init = [0] * n
        for _ in range(m):
            f.append(f_init)
        for i in range(n):
            f[0][i] = 1
        for i in range(m):
            f[i][0] = 1
        # 简化构造
        # f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 4))