


class Queue:
    def __init__(self, val=None):
        if not val:
            self._q = list()
        else:
            self._q = [val]

    def put(self, val):
        self._q = self._q + [val]
        return True

    def get(self):
        if self.size() <= 0:
            return -1
        v = self._q[-1]
        self._q = self._q[:-1]
        return v

    def size(self):
        return len(self._q)

    def print(self):
        print(self._q)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        width = 0
        if not root:
            return width

        Q = Queue(root)
        
        while True:
            child = list()
            if Q.size():
                curr = Q.get()
                child.append(curr.left)
                child.append(curr.right)
            else:
                childLen = len(child)
                end = True
                for i in child:
                    if i:
                        end = False
                        Q.put(i)
                if end:
                    return width
                else:
                    width = max(width, childLen)

if __name__ == "__main__":
    print(Solution().widthOfBinaryTree([1,3,2,5,None,None,9,6,None,7]))