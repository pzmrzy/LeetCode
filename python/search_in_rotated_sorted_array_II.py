class Solution(object):
    def find(self, l, r, target, nums):
        if l > r:
            return -1
        mid = (l + r) / 2
        if target == nums[mid]:
            return mid
        if nums[mid] < nums[r]:
            if nums[mid] < target <= nums[r]:
                return self.find(mid + 1, r, target, nums)
            else:
                return self.find(l, mid - 1, target, nums)
        else:
            if nums[l] <= target < nums[mid]:
                return self.find(l, mid - 1, target, nums)
            else:
                return self.find(mid + 1, r, target, nums)
                
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        new = [nums[0]]
        for n in nums[1:]:
            if n != new[-1]:
                new.append(n)
        l = 0
        r = len(new) - 1
        if self.find(l, r, target, new) == -1:
            return False
        else:
            return True
