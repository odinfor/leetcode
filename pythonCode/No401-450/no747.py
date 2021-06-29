#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 6:21 下午
# @Site    : 
# @File    : no747.py
# @desc    :
class Solution:
    def dominantIndex(self, nums: list) -> int:
        m = max(nums)
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.dominantIndex([3,6,1,0]))
    # print(s.dominantIndex([1,2,3,4]))
    print(s.dominantIndex([0,0,0,1]))
    print(s.dominantIndex([0,1,1,2]))