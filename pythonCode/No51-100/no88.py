#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 4:56 下午
# @Site    : 
# @File    : no88.py
# @desc    :
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        方法一：合并nums1，nums2，对nums1进行排序
        方法二：双指针从后向前合并
        """
        if m == 0:
            return nums2
        if n == 0:
            return nums1

        nums1_number_end, nums2_end, nums1_end = m - 1, n - 1, m + n -1
        while True:
            


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
