#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 3:35 下午
# @Site    : 
# @File    : no111.py
# @desc    :

from collections import deque


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """BFS"""
        if not root:
            return 0

        p_list, num = [root], 1

        while True:
            c_list = list()
            # 添加子节点列表
            for i in p_list:
                if not i.left and not i.right:
                    return num
                if i.left: c_list.append(i.left)
                if i.right: c_list.append(i.right)
            num += 1
            p_list = c_list

    def minDepthDfs(self, root: TreeNode) -> int:
        """DFS"""
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_deep = 2 ** 10
        if root.left:
            min_deep = min(min_deep, self.minDepthDfs(root.left))
        if root.right:
            min_deep = min(min_deep, self.minDepthDfs(root.right))

        return min_deep + 1


if __name__ == "__main__":
    t = Tree()
    t.construct_tree([10, 5, 20, 1, None, 11, 30])
    print(t.bfs())
    print(t.pre_traversal())
    print(t.in_traversal())
    print(t.post_traversal())