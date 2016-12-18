# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l = 1
        newh = tail = head
        while tail.next:
            l += 1
            tail = tail.next
        tail.next = head
        k %= l
        if k:
            for i in range(l - k):
                tail = tail.next
        newh = tail.next
        tail.next = None
        return newh
