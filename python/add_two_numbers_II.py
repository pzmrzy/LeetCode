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
        s1 = []
        s2 = []
        while l1 is not None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2.append(l2.val)
            l2 = l2.next
        tmp = 0
        res = ListNode(0)
        while len(s1) != 0 or len(s2) != 0:
            if len(s1) != 0:
                tmp += s1.pop()
            if len(s2) != 0:
                tmp += s2.pop()
            res.val = tmp % 10
            head = ListNode(tmp // 10)
            head.next = res
            res = head
            tmp //= 10
        return res.next if res.val == 0 else res
