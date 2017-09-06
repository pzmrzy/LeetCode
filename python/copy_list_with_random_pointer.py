# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
from collections import defaultdict
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        tmp = head
        dic = defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        while tmp:
            dic[tmp].label = tmp.label
            dic[tmp].next = dic[tmp.next]
            dic[tmp].random = dic[tmp.random]
            tmp = tmp.next
        del dic[None]
        return dic[head]
