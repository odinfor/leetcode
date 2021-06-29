#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 3:29 下午
# @Site    : 
# @File    : no141.py
# @desc    : 给定一个链表，判断链表中是否有环。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycle2(self, head: ListNode) -> bool:
        number_set = set()

        while head:
            if head in number_set:
                return True
            number_set.add(head)
            head = head.next

        return False
