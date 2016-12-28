class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return true
        s = sum(nums)
        if s % 2 != 0:
            return False
        s /= 2
        data = [False] * (s + 1)
        data[0] = True
        for i in range(n):
            for j in range(s, nums[i - 1] - 1, -1):
                data[j] = data[j] or data[j - nums[i - 1]]
        return data[s]
