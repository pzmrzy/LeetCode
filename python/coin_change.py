class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        M = float('inf')
        dp = [0] + [M] * amount
        for i in range(1, amount + 1):
            tmp = M
            for c in coins:
                if i - c >= 0:
                    tmp = min(tmp, dp[i - c])
            dp[i] = tmp + 1
        return dp[amount] if dp[amount] != M else -1
