#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 5:02 下午
# @Site    : 
# @File    : 4.py
# @desc    :
class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        for sub_m in matrix:
            if not sub_m:
                continue
            if target < sub_m[0]:
                return False
            elif sub_m[0] <= target <= sub_m[-1]:
                for y in sub_m:
                    if y == target:
                        return True
                    elif y > target:
                        break

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))