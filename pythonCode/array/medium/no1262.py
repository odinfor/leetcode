#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 3:56 下午
# @Site    : 
# @File    : no1262.py
# @desc    : 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。

class Solution:
    def maxSumDivThree(self, nums: list) -> int:
        """
        按照数学思想:整除3余数只有两种情况，余数1和余数2
        当余数为1时，需要剔除 一个余数为1的数或者2个余数为2的数。当余数为2时，需要剔除 一个余数为2的数或者2个余数为1的数
        将原数组中余数为1和余数为2的数找出并按照降序排序，响应剔除最后的即可
        """
        nums1 = sorted([x for x in nums if x % 3 == 1], reverse=True)
        nums2 = sorted([x for x in nums if x % 3 == 2], reverse=True)

        maxSum, total = 0, sum(nums)

        if total % 3 == 0:
            maxSum = total
        elif total % 3 == 1:
            if len(nums1) >= 1:
                maxSum = max(maxSum, total - nums1[-1])
            if len(nums2) >= 2:
                maxSum = max(maxSum, total - sum(nums2[-2:]))
        elif total % 3 == 2:
            if len(nums1) >= 2:
                maxSum = max(maxSum, total - sum(nums1[-2:]))
            if len(nums2) >= 1:
                maxSum = max(maxSum, total - nums2[-1])

        return maxSum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSumDivThree([3, 6, 5, 1, 8]))
    print(s.maxSumDivThree([4]))
    print(s.maxSumDivThree([2,6,2,2,7]))
