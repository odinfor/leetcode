#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 10:04 上午
# @Site    : 
# @File    : 206反转链表.py
# @desc    : 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None     # 定义None节点,反转后head需要指向None
        curr = head
        while curr:
            temp = curr.next    # 先存下curr的下一个节点记为temp,因为反转后节点指向前节点了不能获取到反转前的当前节点的下一个节点
            curr.next = prev    # 反转链表指针
            prev = curr         # 修改上一个节点
            curr = temp         # 遍历链表

        return prev
