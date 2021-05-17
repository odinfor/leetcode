#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 4:28 下午
# @Site    : 
# @File    : no26.py
# @desc    :
class Solution:
    # 保利破解，超时
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        left = 0
        while True:
            right = len(nums) - 1
            if left >= right:
                break
            while True:
                if right <= left:
                    break
                if nums[left] == nums[right]:
                    nums.pop(right)
                right = right - 1
            left += 1
        print(nums)
        return len(nums)

    def removeDuplicates1(self, nums: list) -> int:
        # 快慢双指针,
        # 快指针位置的值和慢指针位置的值不相同快慢指针右移动一位，
        # 相同快指针右移一位直到快慢指针位置的值不同，慢指针右移一位并将该位置的值修改为快指针位置的值。
        # 快指针走到最后返回慢指针的位置长度
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        slow, fast, nextDiffranceNeedChange = 0, 1, False
        while fast <= len(nums) - 1:
            if nums[slow] == nums[fast]:
                nextDiffranceNeedChange = True
            if nums[slow] != nums[fast]:
                if nextDiffranceNeedChange:
                    slow += 1
                    nums[slow] = nums[fast]
                if not nextDiffranceNeedChange:
                    slow += 1
            fast += 1
        print(nums)
        return slow + 1, nums[:slow+1]


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 2, 2, 5, 6, 7, 7, 7, 9, 12, 12, 15]))
    print(s.removeDuplicates1([1, 2, 2, 5, 6, 7, 7, 7, 9, 12, 12, 15]))
    print(s.removeDuplicates1([1, 1]))
