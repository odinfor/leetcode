#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 11:12 上午
# @Site    : 
# @File    : no75.py
# @desc    :
class Solution:
    def sortColors(self, nums: list) -> None:
        """
        三指针：头尾指针不动，中间指针i遍历，nums[i]==0和头指针互换,nums[i]==2和尾指针互换。互换位置后头指针右移，尾指针左移。直到i>右指针
        """
        p0, p2, i = 0, len(nums) - 1, 0

        while i <= p2:
            if nums[i] == 2 and i < p2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0 and i > p0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            else:
                i += 1

        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.sortColors([2, 0, 2, 1, 0, 1])