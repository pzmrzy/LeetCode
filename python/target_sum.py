class Solution(object):
    def dp(self, nums, i, summ, S, data):
        if i == len(nums):
            if S == summ:
                return 1
            else:
                return 0
        else:
            if data[i][summ + 1000] != float('-inf'):
                return data[i][summ + 1000]
            add = self.dp(nums, i + 1, summ + nums[i], S, data)
            sub = self.dp(nums, i + 1, summ - nums[i], S, data)
            data[i][summ + 1000] = add + sub
            return data[i][summ + 1000]
            
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        data = [[float('-inf') for i in range(2001)] for _ in range(len(nums))]
        return self.dp(nums, 0, 0, S, data)
