#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 3:23 下午
# @Site    : 
# @File    : 496下一个更大元素I.py
# @desc    : 给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。请你找出 nums1中每个元素在nums2中的下一个比其大的值。
#            nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        nums2_map, next_index_list, nums2_len = dict(), list(), len(nums2)
        nums3 = sorted(nums2)
        for i in nums1:
            if i == nums3[-1]:
                next_index_list.append(-1)
                continue
            nums2_index, nums3_index = nums2.index(i), nums3.index(i)
            if nums2_index == nums2_len - 1:
                next_index_list.append(-1)
            else:
                next_index = nums3_index + 1
                next_index_list.append(nums2.index(nums3[next_index]))

        return next_index_list


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(s.nextGreaterElement([2, 4], [1,2,3,4]))

