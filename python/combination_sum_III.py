import Queue
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        q = Queue.Queue()
        res = []
        q.put( [[], 1, n] )
        while not q.empty():
            now, i, c = q.get()
            if len(now) == k and c == 0:
                res.append(now)
            else:
                if len(now) == k:
                    continue
                if i == 10:
                    continue
                for j in range(i, 10):
                    x = now + [j]
                    t = c-j
                    if t >= 0:
                        q.put([x, j+1, c - j])
        return res
