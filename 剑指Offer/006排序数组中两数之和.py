#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 5:53 下午
# @Site    : 
# @File    : 006排序数组中两数之和.py
# @desc    : 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        """双指针"""
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
