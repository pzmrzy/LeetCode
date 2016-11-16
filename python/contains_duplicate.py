class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sets = set()
        for n in nums:
            if n in sets:
                return True
            else:
                sets.add(n)
        return False
