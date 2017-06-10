class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l = len(nums)
        if l == 1:
            return str(nums[0])
        if l == 2:
            return "%s/%s" % (nums[0], nums[1])
        return "%s/(%s)" % (nums[0], '/'.join(map(str, nums[1:])))
