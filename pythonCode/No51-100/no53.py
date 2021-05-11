#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 5:59 下午
# @Site    : 
# @File    : no53.py
# @desc    :
class Solution:
    def maxSubArray(self, nums) -> int:
        left, right, maxSum = 0, len(nums) - 1, 0

        while left <= right:
            newSum = self.getSum(nums[left: right])
            maxSum = newSum if newSum > maxSum else maxSum
            if left == right:
                if nums[left] > 0:
                    maxSum = maxSum + nums[left]
                    return maxSum
            if nums[left] < 0 and nums[right] > 0:
                left += 1
            elif nums[left] > 0 and nums[right] < 0:
                right -= 1
            elif nums[left] > nums[right]:
                right -= 1
            else:
                left += 1

        return maxSum

    def getSum(self, nums):
        num = 0
        for i in nums:
            num += i
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


