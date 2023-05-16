#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     """
    #     快慢双指针思路,需要先计算链表长度再移动指针，时间复杂度2*O(n)
    #     """
    #     if not head:
    #         return head
    #     nodeLen = 0
    #     lenHead = head
    #     # 计算链表长度
    #     while lenHead:
    #         nodeLen += 1
    #         lenHead = lenHead.next
            
    #     # k可能大于链表长度，旋转时旋转链表长度的次数相当于没有改变
    #     step = k % nodeLen
    #     if not step:
    #         return head

    #     l, r = head, head
    #     while step > 0: # 右指针左移k个位置
    #         r = r.next
    #         step -= 1

    #     while r.next:
    #         l = l.next
    #         r = r.next
        
    #     temp = l.next
    #     l.next = None
    #     r.next = head
    #     return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        循环链表思路
        """
        if not head:
            return head

        curr, nodeLen = head, 1
        while curr: # 建立循环
            if curr.next:
                curr = curr.next
                nodeLen += 1
            else:
                curr.next = head
                break
        for _ in range(nodeLen - (k % nodeLen)):
            curr = curr.next
        
        head = curr.next
        curr.next = None
        return head
        


        
# @lc code=end

