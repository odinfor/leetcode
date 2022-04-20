#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 3:59 下午
# @Site    : 
# @File    : no643子数组最大平均数1.py
# @desc    :

class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        if k >= len(nums):
            return sum(nums) / k
        max_num = sum(nums[:4])
        left, right = 0, k - 1
        while right < len(nums) - 1:
            left += 1
            right += 1
            max_num = max(max_num, max_num - nums[left - 1] + nums[right])

        return max_num / k