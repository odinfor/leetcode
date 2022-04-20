#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2"0"22/3/9 11:34 上午
# @Site    : 
# @File    : no2"0""0"岛屿数量.py
# @desc    :

class Solution:
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0
        count = 0
        row, column = len(grid), len(grid[0])
        for y in range(row):
            for x in range(column):
                if grid[y][x] == "1":
                    count += 1
                self.__dfs(grid, y, x)

        return count

    def __dfs(self, grid, row, column):
        # 判断是否超出边界
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            return
        if grid[row][column] != "1":   # 不是岛屿直接返回
            return
        grid[row][column] = "2"    # 修改岛屿的值,避免重复计算
        self.__dfs(grid, row - 1, column)
        self.__dfs(grid, row + 1, column)
        self.__dfs(grid, row, column + 1)
        self.__dfs(grid, row, column - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
        ])
    )
    print(s.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ])
    )