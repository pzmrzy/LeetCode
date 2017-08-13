class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            new_res = []
            for l in res:
                for i in range(len(l) + 1):
                    new_res.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            res = new_res
        return res
