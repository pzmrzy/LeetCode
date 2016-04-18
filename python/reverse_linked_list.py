# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        tail = None
        while (head.next != None):
            now = head.next
            head.next = tail
            tail = head
            head = now
        head.next = tail
        return head
