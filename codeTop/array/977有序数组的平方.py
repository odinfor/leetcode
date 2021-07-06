#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 6:07 下午
# @Site    : 
# @File    : 977有序数组的平方.py
# @desc    : 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

class Solution:
    def sortedSquares(self, nums: list) -> list:
        s = [x * x for x in nums]
        s.sort()
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-7,-3,2,3,11]))