#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 2:38 下午
# @Site    : 
# @File    : no128.py
# @desc    : 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

class Solution:
    def longestConsecutive(self, nums: list) -> int:
            nums = list(set(nums))
            nums.sort()
            if not nums:
                return 0
            if len(nums) == 1:
                return 1

            left, max_len = int(), int()

            for i in range(len(nums)):
                if i == 0:
                    continue
                if nums[i] - nums[i - 1] != 1:
                    max_len = max(max_len, i - left)
                    left = i
                elif nums[i] - nums[i - 1] == 1 and i == len(nums) - 1:
                    max_len = max(max_len, i - left + 1)

            return max_len


if __name__ == "__main__":
    s = Solution()
    # print(s.longestConsecutive([100,4,200,1,3,2]))
    # print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    # print(s.longestConsecutive([1,2,0,1]))
    print(s.longestConsecutive([100,4,200,1,3,2]))