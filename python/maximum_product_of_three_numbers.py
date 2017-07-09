class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = sorted(nums)
        if len(nums) > 6:
            N = N[:3] + N[-3:]
        l = len(N)
        return max(N[i] * N[j] * N[k] for i in range(l) for j in range(i + 1, l) for k in range(j + 1, l))
