#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 11:35 上午
# @Site    : 
# @File    : no27.py
# @desc    :
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        """
        不能使用新的数组空间：解题思想还是快慢双指针
        1.找到第一个不等于val的值的位置，作为左指针，右移一位的位置左右右指针
        2.右指针的值右移等于val，左右指针的值互换，左指针+1，否则右指针+1
        3.得到最后nums[:left]均为值等于val的，[left:]均为不等于val的
        """
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        elif len(nums) == 1 and nums[0] != val:
            return 1
        left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                left = i
                break
            if i == len(nums) - 1:
                print([])
                return 0

        right = left + 1
        while right <= len(nums) - 1:
            if nums[right] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        print(nums[left:])
        return len(nums[left:])


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([2, 3, 3, 2], 3))
    print(s.removeElement([2, 2], 2))
    print(s.removeElement([3, 2, 2, 3], 3))




