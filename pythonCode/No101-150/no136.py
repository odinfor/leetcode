#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 6:35 下午
# @Site    : 
# @File    : no136.py
# @desc    :

class Solution:
    def singleNumber(self, nums: list) -> int:
        nums.sort()
        left = 0

        while left < len(nums) - 1:
            right = left + 1
            if nums[left] != nums[right]:
                return nums[left]
            else:
                left += 2

        return nums[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))

