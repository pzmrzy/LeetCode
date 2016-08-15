ass Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return r+1
        while True:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if l == r:
                if target > nums[l]:
                    return r
                else:
                    return l
            if l + 1 == r:
                return r
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
