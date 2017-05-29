class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = {}
        dic2 = {}
        for i, r in enumerate(list1):
            dic1[r] = i
        for i, r in enumerate(list2):
            dic2[r] = i
        resn = 10000
        resd = {}
        for r in list1:
            if r in list2:
                t = dic1[r] + dic2[r]
                resd.setdefault(t, [])
                resd[t].append(r)
        resn = min(resd.keys())
        return resd[resn]
        
