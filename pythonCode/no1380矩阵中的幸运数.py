#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 6:44 下午
# @Site    : 
# @File    : no1380矩阵中的幸运数.py
# @desc    :

class Solution:
    def luckyNumbers (self, matrix: list) -> list:
        res = []
        if not matrix:
            return res
        if not matrix[0]:
            return res
        rows, columns = len(matrix), len(matrix[0])
        for r in range(rows):
            min_x = min(matrix[r])
            idx = matrix[r].index(min_x)
            min_y = [i[idx] for i in matrix]
            if min_x == max(min_y):
                res.append(min_x)
            else:
                continue
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))