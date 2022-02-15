#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 6:11 下午
# @Site    : 
# @File    : no64.py
# @desc    :

class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid or not grid[0]:
            return 0

        row, wight, start_num = len(grid) - 1, len(grid[0]) - 1, 0
        start_num += grid[row][wight]

        while row >= 0 and wight >= 0:
            if row - 1 >= 0 and wight - 1 >= 0:
                if grid[row - 1][wight] < grid[row][wight - 1]:
                    start_num += grid[row - 1][wight]
                    row -= 1
                else:
                    start_num += grid[row][wight - 1]
                    wight -= 1
            if row - 1 < 0 and wight - 1 >= 0:
                start_num += grid[row][wight - 1]
                wight -= 1
            if wight - 1 < 0 and row - 1 >= 0:
                start_num += grid[row - 1][wight]
                row -= 1

    def minPathSum2(self, grid: list) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum2([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum2([[1,2,3],[4,5,6]]))
