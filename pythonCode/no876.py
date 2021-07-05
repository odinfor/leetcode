#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 4:40 下午
# @Site    : 
# @File    : no876.py
# @desc    : 给定一个头结点为 head 的非空单链表，返回链表的中间结点。如果有两个中间结点，则返回第二个中间结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 双指针，寻找中点，左指针步长1，右指针步长2.右指针移动到最后节点时返回左指针的下一个节点即可
        left, right = head, head

        while right:
            if right.next is None:
                return left
            elif right.next.next is None:
                return left.next

            left = left.next
            right = right.next.next


