import Queue
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        q = Queue.Queue()
        res = []
        q.put( [[], nums] )
        while not q.empty():
            now, c = q.get()
            if len(now) == n:
                res.append(now)
            else:
                lc = len(c)
                for i in range(lc):
                    x = now + [c[i]]
                    t = c[:]
                    t.remove(c[i])
                    q.put([x, t])
        return res
