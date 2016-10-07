import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dif = sys.maxint
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == target:
                    return target
                if abs(target - t) < dif:
                    dif = abs(target - t)
                    res = t
                if t < target:
                    l += 1
                else:
                    r -= 1
        return res
