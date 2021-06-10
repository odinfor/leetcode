#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 6:25 下午
# @Site    : 
# @File    : no67.py
# @desc    :
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_end, b_end, res = len(a) - 1, len(b) - 1, str()
        need_add_one = False
        while True:
            if b_end >= 0 and a_end >= 0:
                if need_add_one:
                    curr_value = int(a[a_end]) + int(b[b_end]) + 1
                    if curr_value > 2:
                        res = "1" + res
                    elif curr_value == 2:
                        res = "0" + res
                    else:
                        need_add_one = False
                        res = "1" + res
                else:
                    curr_value = int(a[a_end]) + int(b[b_end])
                    if curr_value == 2:
                        res = "0" + res
                        need_add_one = True
                b_end -= 1
                a_end -= 1
            



