#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 5:39 下午
# @Site    : 
# @File    : no86分割链表.py
# @desc    : 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#            你应当 保留 两个分区中每个节点的初始相对位置。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        curr = head
        smallListNode, bigListNode = ListNode(val=None), ListNode(val=None)
        smallFirstNode, bigFirstNode = None, None

        while curr:
            if curr.val < x and smallListNode.val is None:
                smallListNode.val = curr.val
                smallFirstNode = smallListNode
            elif curr.val < x and smallListNode.val is not None:
                smallListNode.next = curr
                smallListNode = smallListNode.next

            if curr.val >= x and bigListNode.val is None:
                bigListNode.val = curr.val
                bigFirstNode = bigListNode
            elif curr.val >= x and bigListNode.val is not None:
                bigListNode.next = curr
                bigListNode = bigListNode.next

            curr = curr.next

        bigListNode.next = None
        if smallFirstNode is None and bigFirstNode is not None:
            return bigFirstNode
        elif smallFirstNode is not None and bigFirstNode is None:
            smallListNode.next = None
            return smallFirstNode
        else:
            smallListNode.next = bigFirstNode
            return smallFirstNode

