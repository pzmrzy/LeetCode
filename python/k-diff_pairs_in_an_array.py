class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0
        dic = {}
        for n in nums:
            dic.setdefault(n, 0)
            dic[n] += 1
        res = 0

        if k == 0:
            for key in dic:
                if dic[key] > 1:
                    res += 1
        else:
            for n in dic:
                if n + k in dic:
                    res += 1
        return res
