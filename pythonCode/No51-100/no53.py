#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 5:59 下午
# @Site    : 
# @File    : no53.py
# @desc    :
class Solution:
    def maxSubArray(self, nums) -> int:
        # 动态规划
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        curMax, resultMax = -100000, nums[0]
        for i in range(len(nums)):
            curMax = max(nums[i] + curMax, nums[i])
            resultMax = max(curMax, resultMax)

        return resultMax


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


