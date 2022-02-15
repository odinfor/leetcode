#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 10:58 上午
# @Site    : 
# @File    : no203移除链表元素.py
# @desc    : 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

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
