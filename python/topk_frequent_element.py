class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            dic.setdefault(n, 0)
            dic[n] += 1
        dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
        res = []
        for i in range(k):
            res.append(dict[i][0])
        return res
