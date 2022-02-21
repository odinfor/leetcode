#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 5:10 下午
# @Site    : 
# @File    : no80删除有序数组中的重复项.py
# @desc    :
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
    print(s.removeDuplicates([1, 2, 2]))
    print(s.removeDuplicates([1,1,1,2,2,2,3,3]))


