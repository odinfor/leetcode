#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/20 5:17 下午
# @Site    : 
# @File    : no704.py
# @desc    : 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

class Solution:
    def search(self, nums: list, target: int) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))