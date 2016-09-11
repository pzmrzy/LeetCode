import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [0]
        n = len(nums)
        for i in range(n):
            sums.append(nums[i] + sums[i])
        maxx = [-sys.maxint]
        for i in range(n):
            if sums[i+1] > maxx[i]:
                maxx.append(sums[i+1])
            else:
                maxx.append(maxx[i])
        minn = [0]
        for i in range(n):
            if sums[i+1] < minn[i]:
                minn.append(sums[i+1])
            else:
                minn.append(minn[i])
        res = -sys.maxint
        for i in range(1, len(sums)):
            res = max(res, sums[i]-minn[i-1])
        return res
