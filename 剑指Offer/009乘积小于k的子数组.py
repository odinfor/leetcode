#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 10:43 上午
# @Site    : 
# @File    : 009乘积小于k的子数组.py
# @desc    : 给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。

class Solution:
    @staticmethod
    def res_of_list(nums: list) -> int:
        res = 1
        for i in nums:
            res = res * i

        return res

    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        nums_len, count = len(nums), 0
        for l in range(1, nums_len + 1):
            start = 0
            while True:
                end = start + l
                if end > nums_len:
                    break
                if self.res_of_list(nums[start: end]) < k:
                    count += 1
                start += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
