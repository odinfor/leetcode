#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 3:53 下午
# @Site    : 
# @File    : no203.py
# @desc    :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start_head = ListNode(next=head)
        curr_node = start_head
        while curr_node.next:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return start_head.next


