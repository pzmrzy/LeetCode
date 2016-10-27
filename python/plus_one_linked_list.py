# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now = None
        dummy = head
        while dummy:
            if dummy.val < 9:
                now = dummy
            dummy = dummy.next
    
        if now:
            now.val += 1
            dummy = now.next
        else:
            new = ListNode(1)
            new.next = head
            node = head
            head = new
            dummy = head.next
            
        while dummy:
            dummy.val = 0
            dummy = dummy.next
    
        return head
