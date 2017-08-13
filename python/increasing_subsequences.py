class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def check(l):
            for i in range(1, len(l)):
                if l[i - 1] > l[i]:
                    return False
            return True
        
        res = []
        for i in range(2, len(nums) + 1):
            res.extend(set(itertools.combinations(nums, i)))
        return [x for x in res if check(x)]
