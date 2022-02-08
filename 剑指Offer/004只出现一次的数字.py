#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 4:37 下午
# @Site    : 
# @File    : 004只出现一次的数字.py
# @desc    : 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#            示例1：输入：nums = [2,2,3,2]， 输出：3
#            示例2：输入：nums = [0,1,0,1,0,1,100]    输出：100
class Solution:
    def singleNumber(self, nums: list) -> int:
        # 利用排序函数
        nums.sort()
        start = 0
        while start < len(nums) - 1:
            if nums[start] == nums[start + 1]:
                start += 3
                continue
            else:
                return nums[start]

        return nums[start]

    def singleNumber2(self, nums: list) -> int:
        # 利用map
        timeMap = dict()
        for i in nums:
            timeMap[i] = timeMap[i] + 1 if timeMap.get(i) else 1

        for k, v in timeMap.items():
            if v == 1: return k
