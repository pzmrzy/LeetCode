# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while True:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = max(mid-1, l)
            else:
                l = min(mid+1, r)
            if l == r:
                if isBadVersion(l):
                    return l
                else:
                    return l + 1
