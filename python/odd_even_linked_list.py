# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyodd = ListNode(0)
        dummyeven = ListNode(0)
        tailodd = dummyodd
        taileven = dummyeven
        p = head
        c = 1
        while p != None:
            if c % 2 == 0:
                taileven.next = p
                taileven = p
            else:
                tailodd.next = p
                tailodd = p
            p = p.next
            c += 1
        tailodd.next = taileven.next = None
        tailodd.next = dummyeven.next
        return dummyodd.next
