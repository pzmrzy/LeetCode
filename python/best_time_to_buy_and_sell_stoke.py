class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minn = prices[0]
        pro = 0
        for p in prices:
            t = p - minn
            if t > pro:
                pro = t
            if p < minn:
                minn = p
        
        return pro
