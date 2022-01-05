#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 5:33 下午
# @Site    : 
# @File    : no257.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self):
#         self.node_path_list = []
#
#     def binaryTreePaths(self, root: TreeNode) -> list:
#         if not root:
#             return []
#
#         curr_path = ""
#         self.getPath(root, curr_path)
#
#     def getPath(self, root: TreeNode, path: str):
#         if not root.right and not root.left:
#             path += "{}".format(root.val)
#             self.node_path_list.append(path)
#             path = ""
#             return
#         else:
#             path += "{}->".format(root.val)
#             self.getPath(root.left, path)
#             self.getPath(root.right, path)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_node_list = []
        self.getLeftSum(root, left_node_list)

        return sum(left_node_list)

    def getLeftSum(self, root: TreeNode, left_node_list: list) -> int:
        if root:
            if not root.left:
                left_node_list.append(root.val)

            self.getLeftSum(root, left_node_list)


