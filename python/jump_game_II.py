class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump = curEnd = curFar = 0
        l = len(nums)
        for i in range(l - 1):
            curFar = max(curFar, i + nums[i])
            if curEnd == i:
                jump += 1
                curEnd = curFar
        return jump
