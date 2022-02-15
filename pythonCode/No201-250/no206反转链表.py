#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 3:23 下午
# @Site    : 
# @File    : no206反转链表.py
# @desc    : 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next    # 中间变量保存curr的下一个节点,当前节点curr需要反转指向
            curr.next = prev    # 反转指针，当前节点指向prev
            prev = curr         # prev往后移一位
            curr = temp         # 使得curr后移遍历head链表

        return prev



