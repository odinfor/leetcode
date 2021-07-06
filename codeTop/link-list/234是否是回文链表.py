#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 11:16 上午
# @Site    : 
# @File    : 234是否是回文链表.py
# @desc    : 请判断一个链表是否为回文链表。

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_map = dict()
        curr, start = head, 0
        while curr:
            node_map[start] = curr.val
            start += 1
            curr = curr.next

        if not node_map:
            return False

        left, right = 0, start - 1
        while left < right:
            if node_map[left] != node_map[right]:
                return False
            left += 1
            right -= 1

        return True
