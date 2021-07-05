#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 2:39 下午
# @Site    : 
# @File    : no83.py
# @desc    :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        curr = head
        while curr.next:    # 第一个节点一定不会删除
            # 当前节点的值和下一个节点的值相同，当前节点指向下下个节点
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:   #
                curr = curr.next

        return head


