import Queue
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = Queue.PriorityQueue()
        for l in matrix:
            q.put(list(l))
        for i in xrange(k-1):
            t = q.get()
            if len(t) > 1:
                q.put(t[1:])
        return q.get()[0]
