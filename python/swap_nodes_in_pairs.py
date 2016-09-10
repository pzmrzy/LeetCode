# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        t1 = head
        t2 = head.next
        t3 = head.next.next
        head = t2
        head.next = t1
        head.next.next = self.swapPairs(t3)
        return head
