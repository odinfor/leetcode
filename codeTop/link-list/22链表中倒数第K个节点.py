#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 11:46 上午
# @Site    : 
# @File    : 22链表中倒数第K个节点.py
# @desc    :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 简单直观想法
        node_list = list()
        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next

        return node_list[len(node_list) - k]

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        # 双指针,左右指针均从头开始，右指针先走k个节点再一起移动。当右节点走到最后左节点即为倒数k的结果节点
        left, right = head, head
        for _ in range(k):
            right = right.next

        while right:
            left = left.next
            right = right.next

        return left
