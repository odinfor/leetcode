#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 4:06 下午
# @Site    : 
# @File    : no143重排链表.py
# @desc    :

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        通过遍历head链表所有节点重构，时间复杂度O(n)空间复杂度O(n)
        """
        if not head:
            return

        # 使用队列存放链表所有节点
        currNode, nodeList = head, []
        while currNode:
            nodeList.append(currNode)
            currNode = currNode.next

        # 双指针重构链表
        left, right = 0, len(nodeList) - 1
        while left < right:
            nodeList[left].next = nodeList[right]
            if left + 1 >= right:
                nodeList[right].next = None
            else:
                nodeList[right].next = nodeList[left + 1]
            left += 1
            right -= 1
        # 修改重构链表最后节点的指针
        nodeList[left].next = None








