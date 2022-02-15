#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 3:56 下午
# @Site    : 
# @File    : no237删除链表中的节点.py
# @desc    : 请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点head ，只能直接访问 要被删除的节点 。
#            题目数据保证需要删除的节点 不是末尾节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        """
        给的node是要删除的节点，并且不能访问头结点，即不能遍历链表。删除节点即修改要删除节点的val为node.next的val，并且指针指向下下个节点即可
        """
        node.val = node.next.val
        node.next = node.next.next