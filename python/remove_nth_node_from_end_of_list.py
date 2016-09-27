# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy1.next = head
        dummy2.next = head
        for i in range(n):
            dummy1 = dummy1.next
        if dummy1.next == None:
            return head.next
        while dummy1.next != None:
            dummy1 = dummy1.next
            dummy2 = dummy2.next
        dummy2.next = dummy2.next.next
        return head
