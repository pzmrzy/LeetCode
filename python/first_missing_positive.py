class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        l = len(nums)
        if l == 1:
            return 1
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0
        for i in range(l):
            nums[nums[i]%l]+=l
        print nums
        for i in range(1, l):
            if nums[i] < l:
                return i
        return l
