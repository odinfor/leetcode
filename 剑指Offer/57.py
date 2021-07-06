#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 5:26 下午
# @Site    : 
# @File    : 57.py
# @desc    :
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return [nums[left], nums[right]]
    