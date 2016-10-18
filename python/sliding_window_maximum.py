class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        dq = []
        for i in range(n):
            while len(dq) > 0 and dq[0] < i - k + 1:
                del dq[0]
            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                del dq[-1]
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res[k - 1:]
