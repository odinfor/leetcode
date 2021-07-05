#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 5:46 下午
# @Site    : 
# @File    : no215.py
# @desc    :
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort()
        print(nums)

        return nums[len(nums) - k]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))