class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x: x[1])
        res, cur = 0, float('-inf')
        for x, y in pairs:
            if cur < x:
                res += 1
                cur = y
        return res
