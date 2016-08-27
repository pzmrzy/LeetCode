class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        n = len(height)
        lmax = height[::-1]
        rmax = [0] * n
        
        for i in range(n-2):
            rmax[i+1] = max(lmax[i], rmax[i])
        rmax = rmax[::-1]
        lmax = [0] * n
        for i in range(n-2):
            lmax[i+1] = max(height[i], lmax[i])
        res = 0
        for i in range(n):
            res += max(min(lmax[i], rmax[i]) - height[i], 0)
        return res
