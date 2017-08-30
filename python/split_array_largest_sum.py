class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(mid):
            ct = cur = 0
            for n in nums:
                cur += n
                if cur > mid:
                    ct += 1
                    if ct >= m:
                        return False
                    cur = n
            return True
            
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) / 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
