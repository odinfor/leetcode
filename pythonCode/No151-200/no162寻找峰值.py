#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 5:31 下午
# @Site    : 
# @File    : no162寻找峰值.py
# @desc    :

class Solution:
    def findPeakElement(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            print(middle)
            if nums[middle - 1] < nums[middle] and nums[middle] > nums[middle + 1]:
                return middle
            elif nums[middle] < nums[middle + 1]:
                left = middle + 1
            elif nums[middle] > nums[middle + 1]:
                right = middle
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1,2,3,1]))