#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 11:25 上午
# @Site    : 
# @File    : no152.py
# @desc    :
class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        minNum, maxNum, resultMax = nums[0], nums[0], -100000

        for i in range(len(nums)):
            if i == 0:
                resultMax = max(resultMax, nums[0])
            else:
                minNum = min(minNum * nums[i], minNum)
                maxNum = max(maxNum * nums[i], maxNum)
