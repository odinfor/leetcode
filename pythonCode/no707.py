#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 10:30 上午
# @Site    : 
# @File    : no707.py
# @desc    : 实现一个链表，包含在链表类中实现这些功能：
# get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第index个节点之前添加值为val的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = NodeList(val=0)

    def getAll(self):
        node_list = list()
        curr = self.head
        while curr is not None:
            node_list.append(curr.val)
            curr = curr.next

        return node_list

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        start_index = 0
        curr = self.head
        while curr.next is not None:
            if start_index == index:
                return curr.next.val
            curr = curr.next
            start_index += 1

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = NodeList(val=val)
        new_head.next = self.head.next
        self.head.next = new_head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail_node = NodeList(val=val)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = tail_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = NodeList(val=val)
        if index <= 0:
            self.addAtHead(val)
        else:
            curr, start_index = self.head, 1
            while curr.next is not None:
                if start_index == index:
                    node.next = curr.next
                    curr.next = node
                    return
                start_index += 1
                curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        node = self.head
        for _ in range(index):
            node = node.next
        if node.next is not None:
            node.next = node.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
print(obj.getAll())
print(obj.get(1))
obj.addAtIndex(1,2)
print(obj.getAll())
obj.deleteAtIndex(1)
print(obj.getAll())