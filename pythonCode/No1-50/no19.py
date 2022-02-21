#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 5:22 下午
# @Site    : 
# @File    : no19.py
# @desc    : 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n:
            return head
        left, right = head, head
        while n:
            right = right.next
            n -= 1
        if not right:
            return ListNode(val=0)
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head



