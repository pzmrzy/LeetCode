# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        res = ListNode(0)
        res.next = p
        c = 0
        while l1 != None or l2 != None:
            t = c
            if l1 != None:
                t += l1.val
            if l2 != None:
                t += l2.val
            tp = ListNode(t % 10)
            c = t / 10
            p.next = tp
            p = p.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if c == 1:
            tp = ListNode(1)
            p.next = tp
        return res.next.next
