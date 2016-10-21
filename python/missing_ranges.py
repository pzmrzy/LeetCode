class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        #nums = list(set(nums))
        now = lower
        res = []
        pre = lower - 1
        for n in nums+[upper+1]:
            if pre == n:
                continue
            else:
                pre = n
            if n == now:
                now += 1
            else:
                res.append( "%s->%s" % (now, n - 1) if now != n - 1 else str(now)  )
                now = n + 1
        return res
