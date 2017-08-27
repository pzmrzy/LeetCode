class Solution(object):
    def checkUp(self, nums):
        n = len(nums)
        flag = 0
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                if flag == 1:
                    return False
                nums[i + 1] = nums[i]
                flag = 1
        return True

    def checkDown(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        flag = 0
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                if flag == 1:
                    return False
                nums[i] = nums[i + 1]
                flag = 1
        return True

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = nums[:]
        return self.checkUp(nums) or self.checkDown(nums1)
