#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 10:23 上午
# @Site    : 
# @File    : no674.py
# @desc    :
class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        if not nums:
            return 0

        left, max_len = 0, 1
        while left < len(nums) - 1:
            right = left + 1
            while right < len(nums):
                if nums[right] > nums[right - 1]:
                    max_len = max(max_len, right - left + 1)
                    right += 1
                else:
                    left = right
                    break
            if right >= len(nums) - 1:
                return max_len

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.findLengthOfLCIS([1,3,5,4,7]))
    print(s.findLengthOfLCIS([2, 2, 2, 2]))
    print(s.findLengthOfLCIS([1, 2, 3, 4, 5, 6]))