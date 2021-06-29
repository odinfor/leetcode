#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 2:45 下午
# @Site    : 
# @File    : no78.py
# @desc    :
class Solution:
    def subsets(self, nums: list) -> list:
        sub_set = list()
        if len(nums) == 1:
            sub_set.append(nums)
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                sub_set.append(nums[:i + 1] + [nums[y]])

        sub_set.append([])

        return sub_set


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))