#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 5:11 下午
# @Site    : 
# @File    : no55.py
# @desc    :

class Solution:
    def canJump(self, nums: list) -> bool:
        nums_len, right_most_index = len(nums), 0
        for i in range(nums_len):
            if i <= right_most_index:
                right_most_index = max(right_most_index, i + nums[i])
                if right_most_index >= nums_len - 1:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    # print(s.canJump([2,3,1,1,4]))
    # print(s.canJump([3,2,1,0,4]))
    print(s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))