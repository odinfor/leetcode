#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 5:29 下午
# @Site    : 
# @File    : no2208将数组和减少一半的最少次数.py
# @desc    :

class Solution:
    def halveArray(self, nums: list) -> int:
        target, time, curr = sum(nums) / 2, 0, sum(nums)
        while curr > target:
            max_value = max(nums)
            idx = nums.index(max_value)
            curr = curr - max_value + max_value / 2
            nums[idx] = max_value / 2
            time += 1

        return time


if __name__ == "__main__":
    s = Solution()
    print(s.halveArray([5,19,8,1]))
