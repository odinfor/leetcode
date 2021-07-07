#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 5:33 下午
# @Site    : 
# @File    : 349两个数组的交集.py
# @desc    : 给定两个数组，编写一个函数来计算它们的交集。

class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        set_nums = set(nums2) if len(nums1) >= len(nums2) else set(nums1)
        len_nums = nums2 if len(nums2) >= len(nums1) else nums1
        child_nums = list()
        for x in set_nums:
            try:
                len_nums.index(x)
            except ValueError:
                continue
            else:
                child_nums.append(x)

        return child_nums


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1,2,2,1], [2, 2]))
    print(s.intersection([4,9,5], [9,4,9,8,4]))
