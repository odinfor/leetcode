#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 5:59 下午
# @Site    : 
# @File    : no206.py
# @desc    :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None   # 定义空节点
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



