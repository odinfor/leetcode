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
        """
        if m == 0:
            return nums2
        if n == 0:
            return nums1

        index1, index2, nums3 = 0, 0, []
        while True:
            x = min(nums1[index1], nums2[index2])
            if nums1[index1] < nums2[index2]:
                index1 += 1
                nums3.append(x)
            elif nums1[index1] > nums2[index2]:
                index2 += 1
                nums3.append(x)
            else:
                nums3 = nums3 + [x] * 2
                index1 += 1
                index2 += 1

            if index1 > len(nums1) - 1 - n:
                nums3 = nums3 + nums2[index2:]
                break
            if index2 > len(nums2) - 1:
                nums3 = nums3 + nums1[index1:len(nums1) - n]
                break

        return nums3


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
