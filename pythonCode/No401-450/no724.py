#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 11:22 上午
# @Site    : 
# @File    : no724.py
# @desc    :
class Solution:
    def pivotIndex(self, nums: list) -> int:
        all_sum, curr_sum = sum(nums), int()
        for i in range(len(nums)):
            if i > 0:
                curr_sum += nums[i - 1]
            if curr_sum == sum(nums[i + 1:]):
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(s.pivotIndex([2, 1, -1]))

