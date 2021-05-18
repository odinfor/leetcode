#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 3:14 下午
# @Site    : 
# @File    : no35.py
# @desc    :
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        没什么说的二分查找
        """
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] < target:
            return 1
        elif len(nums) == 1 and nums[0] >= target:
            return 0

        left, right = 0, len(nums) - 1
        if target > nums[right]:
            return right + 1
        if target < nums[left]:
            return left

        while left < right:
            mid = left + int((right - left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target <= nums[mid + 1]:
                return mid + 1
            elif target > nums[mid] and target > nums[mid + 1]:
                left = mid + 1
            elif nums[mid - 1] < target < nums[mid]:
                return mid
            elif target < nums[mid - 1]:
                right = mid - 1

        return mid


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 4, 6, 8, 12, 14, 15, 25, 33, 65, 74, 75, 76, 77, 80], 4))
    print(s.searchInsert([1, 3, 5, 6], ))

