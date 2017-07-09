class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        order = [x == y for x, y in zip(nums, sorted(nums))]
        return 0 if all(order) else (len(nums)) - order.index(False) - order[::-1].index(False)
