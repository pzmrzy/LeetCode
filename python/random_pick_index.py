import random
import sys
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.k = 1
        self.l = len(nums)
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = None
        for i in range(self.l):
            if self.nums[i] == target:
                if cnt < self.k:
                    res = i
                else:
                    r = random.randint(0, cnt)
                    if r < self.k:
                        res = i
                cnt += 1
        return res
                        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
