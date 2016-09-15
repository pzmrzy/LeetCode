import random
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.k = 1
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cnt = 0
        now = self.head
        res = None
        while now != None:
            if cnt < self.k:
                res = now.val
            else:
                r = random.randint(0, cnt)
                if r == 0:
                    res = now.val
            cnt += 1
            now = now.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
