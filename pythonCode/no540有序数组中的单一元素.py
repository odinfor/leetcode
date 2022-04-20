#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 4:26 下午
# @Site    : 
# @File    : no540有序数组中的单一元素.py
# @desc    :
class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        """
        题意说明，nums一定是奇数长度的数组,二分中间值将左右分割两部分，长度均为偶数.并且nums中出现相邻元素只有2个，不会多个
        于是若mid左右两边分别和mid-1和mid+1比较，若相等则说明奇数元素出现在另外一边
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]