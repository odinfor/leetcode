#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 6:51 下午
# @Site    : 
# @File    : no686.py
# @desc    :

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        