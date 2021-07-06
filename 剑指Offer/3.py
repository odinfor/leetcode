#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 4:58 下午
# @Site    : 
# @File    : 3.py
# @desc    :在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字
#           重复了几次。请找出数组中任意一个重复的数字。
#

class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        nums_map = dict()
        for i in nums:
            if nums_map.get(i):
                return i
            else:
                nums_map[i] = 1


if __name__ == "__main__":
    s = Solution()
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))