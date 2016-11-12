# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = p = ListNode(-1)
        heap = []
        for i in lists:
            if i:
                heappush(heap,(i.val,i))
        while heap:
            small = heappop(heap)[1]
            p.next = small
            if small.next:
                heappush(heap,(small.next.val,small.next))
            p = small
            p.next = None
        return head.next
