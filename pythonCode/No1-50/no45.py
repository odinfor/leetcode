#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 4:42 下午
# @Site    : 
# @File    : no45.py
# @desc    :

class Solution:
    def jump(self, nums: list) -> int:
        if not nums or len(nums) == 1:
            return 0

        jump_num, start_index = 0, 0
        while start_index < len(nums):
            left, right = start_index + 1, start_index + 1 + nums[start_index]
            max_sub_num = 0

            if right > len(nums) - 1:
                jump_num += 1
                break

            for x in range(left, right):
                if nums[x] + x >= max_sub_num:
                    max_sub_num, start_index = nums[x] + x, x
            jump_num += 1
            if start_index == len(nums) - 1:
                break
            if start_index + nums[x] > len(nums):
                jump_num += 1
                break

        return jump_num


if __name__ == "__main__":
    s = Solution()
    print(s.jump([10,9,8,7,6,5,4,3,2,1,1,0]))
    # print(s.jump([1, 2, 1, 1, 1]))
