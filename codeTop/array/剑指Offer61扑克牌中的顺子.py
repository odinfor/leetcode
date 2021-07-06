#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 5:38 下午
# @Site    : 
# @File    : 剑指Offer61扑克牌中的顺子.py
# @desc    : 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

class Solution:
    def isStraight(self, nums: list) -> bool:
        # 1.有重复的非0项直接返回False；2.计算间隔的牌数和大小王的数量，大小王的数量>=缺失的牌数返回True
        if len(nums) < 5 or min(nums) > 9:
            return False

        nums.sort()
        num_0, miss_card_num = int(), int()
        for i in range(len(nums)):
            if nums[i] == 0:
                num_0 += 1
                continue
            if i != 0 and nums[i] != 0 and nums[i - 1] != 0:
                if nums[i] == nums[i - 1]:
                    return False
                miss_card_num += nums[i] - nums[i - 1] - 1

        return True if miss_card_num <= num_0 else False


if __name__ == "__main__":
    s = Solution()
    print(s.isStraight([1,2,3,4,5]))
    print(s.isStraight([0,0,1,2,5]))