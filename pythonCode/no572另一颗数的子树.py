#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 9:57 上午
# @Site    : 
# @File    : no572另一颗数的子树.py
# @desc    : 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root and subRoot:
            return False

        subQueue = self.__bfs(subRoot)
        if root.val == subRoot.val:
            rootQueue = self.__bfs(root)
            if subQueue in rootQueue or subQueue == rootQueue:
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def __bfs(self, root: TreeNode):
        inQueue, outQueue = list(), list()  # 压入队列和弹出队列
        # 压入队列
        inQueue.append(root)
        # 弹出压入队列中元素到弹出队列
        while inQueue:
            popNode = inQueue[0]
            inQueue.pop(0)
            if popNode.left:
                inQueue.append(popNode.left)
            if popNode.right:
                inQueue.append(popNode.right)
            outQueue.append(popNode.val)

        return outQueue



