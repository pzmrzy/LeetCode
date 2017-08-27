class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l, r = 0, m * n
        while l != r:
            mid, val = (l + r) / 2, 0
            for i in range(1, m + 1):
                val += min(mid / i, n)
            if val < k:
                l = mid + 1
            else:
                r = mid
        return l
