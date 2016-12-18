class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tmp = minutesToTest / minutesToDie + 1
        now, res = 1, 0
        while now < buckets:
            res += 1
            now *= tmp
        return res
