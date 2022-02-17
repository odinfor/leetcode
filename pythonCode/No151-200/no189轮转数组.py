#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 9:58 上午
# @Site    : 
# @File    : no189轮转数组.py
# @desc    :

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < 0:
            return
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        start_left, start_right, end_left, end_right = 0, k % len(nums), (k % len(nums)) - 1, len(nums) - 1
        while start_left < end_left:
            nums[start_left], nums[end_left] = nums[end_left], nums[start_left]
            start_left += 1
            end_left -= 1
        while start_right < end_right:
            nums[start_right], nums[end_right] = nums[end_right], nums[start_right]
            start_right += 1
            end_right -= 1

        print(nums)
        print(3 % 7)


if __name__ == "__main__":
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)