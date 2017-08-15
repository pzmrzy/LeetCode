class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        now = 1
        if l < 2:
            return l
        for i in range(1, l):
            if nums[i] != nums[i - 1]:
                nums[now] = nums[i]
                now += 1
        return now

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        if res <= 1:
            return res
        now = nums[0]
        k = 0
        for i in range(len(nums)-1):
            x = nums[i+1-k]
            if now == x:
                res -= 1
                del nums[i-k]
                k+=1
            now = x
            
        return res
