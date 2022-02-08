#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 4:56 下午
# @Site    : 
# @File    : 005单词长度的最大乘积.py
# @desc    : 给定一个字符串数组words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
#            示例1：输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
#            输出: 16
#            解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
class Solution:
    def maxProduct(self, words: list) -> int:
