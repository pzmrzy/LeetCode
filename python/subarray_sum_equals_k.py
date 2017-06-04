class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = cs = 0
        dic = collections.defaultdict(lambda: 0)
        dic[0] = 1
        for n in nums:
            cs += n
            res += dic[cs - k]
            dic[cs] += 1
        return res
