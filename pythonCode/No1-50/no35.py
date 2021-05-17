#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 3:14 下午
# @Site    : 
# @File    : no35.py
# @desc    :
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        没什么说的二分查找
        """
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] < target:
            return 1
        elif len(nums) == 1 and nums[0] >= target:
            return 0

        midone = len(nums)/2 + 1

        left, right = nums[:midone], nums[midone:]
