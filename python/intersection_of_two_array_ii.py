class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        for n in nums1:
            dic1.setdefault(n, 0)
            dic2.setdefault(n, 0)
            dic1[n] += 1
        for n in nums2:
            dic2.setdefault(n, 0)
            dic2[n] += 1
        res = []
        for key in dic1:
            res += [key] * min(dic1[key], dic2[key])
        return res
