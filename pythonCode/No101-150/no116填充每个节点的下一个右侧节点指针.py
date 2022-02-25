
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> 'Optional[Node]':
        if not root:
            return root
        nodeQueue = []
        nodeQueue.append(root)
        nodeQueue[0].next = None
        while nodeQueue:
            for i in range(len(nodeQueue)):
                if nodeQueue[0].left:
                    nodeQueue.append(nodeQueue[0].left)
                if nodeQueue[0].right:
                    nodeQueue.append(nodeQueue[0].right)
                nodeQueue.pop(0)
            for i in range(len(nodeQueue) - 1):
                nodeQueue[i].next = nodeQueue[i + 1]
            if len(nodeQueue) != 0:
                nodeQueue[-1].next = None
        return root
