# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        h = head
        while head.next != None:
            while head.val == head.next.val:
                head.next = head.next.next
                if head.next == None:
                    break
            head = head.next
            if head == None:
                break
        return h
