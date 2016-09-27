class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        count = [0] * (l + 1)
        for c in citations:
            count[min(c, l)] += 1
        res = 0
        for i in range(l, -1, -1):
            res += count[i]
            if res >= i:
                return i
