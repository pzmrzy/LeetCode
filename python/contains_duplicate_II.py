class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        l = len(nums)
        for i in xrange(l):
            dic.setdefault(nums[i], [])
            dic[nums[i]].append(i)
        for key in dic:
            value = dic[key]
            for i in xrange(len(value)-1):
                if value[i+1] - value[i] <= k:
                    return True
        return False
