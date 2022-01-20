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
        left = right = head
        for _ in range(n):
            right = right.next

        # 判断是否是最后一个,right是最后一个意味着需要剔除的是第一个节点
        if not right.next:
            return head.next

        # 遍历right剩下的,遍历到最后left的下一个即为需要剔除的节点
        while right.next:
            left = left.next
            right = right.next

        # 指向下下个节点剔除倒数第n个节点
        left.next = left.next.next

        return head

