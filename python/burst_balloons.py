class Solution(object):
    def dp(self, nums, i, j):
        if i + 1 == j:
            return 0
        if self.data[i][j] != -1:
            return self.data[i][j]
        tmp = 0
        for k in range(i+1, j):
            tmp = max(tmp, nums[i] * nums[k] * nums[j] + self.dp(nums, i, k) + self.dp(nums, k, j))
        self.data[i][j] = tmp
        return tmp
        
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[0] * nums[1] + max(nums[0], nums[1])
        nums = [1] + nums + [1]
        n += 2
        self.data = [[-1 for _ in range(n)] for i in range(n)]
        return self.dp(nums, 0, n-1)
