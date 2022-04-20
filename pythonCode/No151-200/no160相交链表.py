#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 3:06 下午
# @Site    : 
# @File    : no160相交链表.py
# @desc    : 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        相交节点：两链表分别从头结点相同步长出发，a链表长度分为x,y两部分.b链表分为z,y两部分，设y为相交的节点后的公共长度。则有x=z或者x+y+z为再次相交相遇的节点
        1.到相同节点则返回
        2.没有找到，则分别从另外一个链表从头开始，在这次中若没有找到相交节点，则不存在相交
        """
        nodeA, nodeB = headA, headB
        firstA, firstB = True, True

        while nodeA or nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            if not nodeA and firstA:
                nodeA = headB
                firstA = False
            if not nodeB and firstB:
                nodeB = headA
                firstB = False
        return None
