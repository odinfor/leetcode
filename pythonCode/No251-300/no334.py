#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 4:10 下午
# @Site    : 
# @File    : no334.py
# @desc    : 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        if len(nums) < 3:
            return False

        dealNum = {}

        for i in range(1, len(nums) - 1):
            if nums[i] in dealNum:
                continue
            leftMin = min(nums[:i])
            rightMax = max(nums[i + 1:])
            if leftMin < nums[i] < rightMax:
                return True
            dealNum[nums[i]] = ""

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1, 2, 3, 4, 5]))
    print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(s.increasingTriplet([20, 100, 10, 12, 5, 13]))