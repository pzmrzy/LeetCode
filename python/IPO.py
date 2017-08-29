from Queue import PriorityQueue
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        res = W
        proq, capq = PriorityQueue(), PriorityQueue()
        for i in range(len(Profits)):
            if Capital[i] <= res:
                proq.put((-Profits[i], Capital[i]))
            else:
                capq.put((Capital[i], Profits[i]))
        for i in range(k):
            if proq.qsize() == 0:
                break
            pro, cap = proq.get()
            res -= pro
            while capq.qsize() > 0:
                tcap, tpro = capq.get()
                if tcap <= res:
                    proq.put((-tpro, tcap))
                else:
                    capq.put((tcap, tpro))
                    break
        return res
