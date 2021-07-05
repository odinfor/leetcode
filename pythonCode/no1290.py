#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 4:59 下午
# @Site    : 
# @File    : no1290.py
# @desc    :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val_list = list()
        num = int()
        while head:
            val_list = [head.val] + val_list
            head = head.next

        for k, v in enumerate(val_list):
            num += (2 ** k) * v

        return num