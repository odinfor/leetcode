#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 6:00 下午
# @Site    : 
# @File    : 008和大于等于target的最短子数组.py
# @desc    : 给定一个含有n个正整数的数组和一个正整数 target 。找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        """滑动窗口"""
        if sum(nums) < target:
            return 0
        max_len, start, end = len(nums), 0, 0
        while start <= len(nums) - 1 and end <= len(nums) - 1:
            if sum(nums[start: end + 1]) < target:
                end += 1
            else:
                max_len = min(max_len, end - start + 1)
                start += 1

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))