class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            tmp = res[:]
            for t in tmp:
                res.append(t+[n])
        return map(list,list(set(map(tuple,[sorted(t) for t in res]))))
