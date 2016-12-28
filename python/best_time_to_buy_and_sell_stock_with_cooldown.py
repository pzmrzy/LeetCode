class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        b0 = b1 = -prices[0]
        s0 = s1 = s2 = 0
        for i in range(n):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1, s2, s1 = b0, s1, s0
        return s0
