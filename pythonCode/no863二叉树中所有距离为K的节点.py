#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 4:52 下午
# @Site    : 
# @File    : no863二叉树中所有距离为K的节点.py
# @desc    :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list:
        """
        分为左子树和右子树
        bfs先找到target所在的deep,通过target所在的左右子树deep，同侧继续下探，异侧计算deep重新bfs
        """
        if not root:
            return []
        res = []
        left_root, right_root = root.left, root.right   # 左右根节点
        left_start_deep, left_target_deep = 1, -1
        right_start_deep, right_target_deep = 1, -1
        left_nodes_map, left_start_nodes = {0: root, 1: [left_root]}, [left_root]
        right_nodes_map, right_start_nodes = {0: root, 1: [right_root]}, [right_root]
        if left_root:
            self.__bfs(left_start_nodes, target, left_start_deep, left_target_deep, left_nodes_map)
        if right_root:
            self.__bfs(right_start_nodes, target, right_start_deep, right_target_deep, right_nodes_map)

        if left_target_deep:
            if left_nodes_map.get(left_target_deep + k):
                res = res + left_nodes_map.get(left_target_deep + k)
            if right_nodes_map.get(k - left_target_deep):
                res = res + right_nodes_map.get(k - left_target_deep)
        if right_target_deep:
            if right_nodes_map.get(right_target_deep + k):
                res = res + right_nodes_map.get(right_target_deep + k)
            if left_nodes_map.get(k - right_target_deep):
                res = res + left_nodes_map.get(k - right_target_deep)
        return res

    def __bfs(self, curr_deep_nodes: list, target: TreeNode, curr_deep: int, target_deep: int, deep_nodes_map: dict):
        next_deep_nodes = list()
        # 获取下一层所有节点
        for node in curr_deep_nodes:
            if node.left == target or node.right == target:
                target_deep = curr_deep + 1
            if node.left:
                next_deep_nodes.append(node.left)
            if node.right:
                next_deep_nodes.append(node.right)
        deep_nodes_map[curr_deep + 1] = next_deep_nodes
        curr_deep_nodes = next_deep_nodes
        curr_deep += 1
        if not curr_deep_nodes:
            return
        return self.__bfs(curr_deep_nodes, target, curr_deep, target_deep, deep_nodes_map)



