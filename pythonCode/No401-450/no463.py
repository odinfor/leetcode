#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 4:17 下午
# @Site    : 
# @File    : no463.py
# @desc    :
class Solution:
    def islandPerimeter(self, grid: list) -> int:
        base_grid, all_gird = 4, 0
        for y in range(len(grid)):
            for x in range(len(y)):
                if grid[y][x] == 0:
                    continue
                if x == 0 and