#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 6:17 下午
# @Site    : 
# @File    : 922按奇偶排序数组II.py
# @desc    : 给定一个非负整数数组A， A 中一半整数是奇数，一半整数是偶数。
#            对数组进行排序，以便当A[i] 为奇数时，i也是奇数；当A[i]为偶数时， i 也是偶数。你可以返回任何满足上述条件的数组作为答案。

class Solution:
    def sortArrayByParityII(self, nums: list) -> list:
        right = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 != 0:
                while right <= len(nums) - 1:
                    if nums[right] % 2 == 0:
                        nums[i], nums[right] = nums[right], nums[i]
                        right += 2
                        break
                    right += 2

        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParityII([4,2,5,7]))
    print(s.sortArrayByParityII([2,0,3,4,1,3]))
    print(s.sortArrayByParityII([4,1,1,0,1,0]))
