import Queue
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        q = Queue.Queue()
        res = []
        q.put( [[], 0, target] )
        n = len(candidates)
        while not q.empty():
            now, i, c = q.get()
            if c == 0:
                tmp = sorted(now)
                if tmp not in res:
                    res.append(tmp)
            else:
                for j in range(i, n):
                    x = now + [candidates[j]]
                    t = c - candidates[j]
                    if t >= 0:
                        q.put([x, j+1, t])
        return res
