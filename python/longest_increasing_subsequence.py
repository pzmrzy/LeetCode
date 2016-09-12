import sys
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [-sys.maxint]
        for n in nums:
            if n > res[-1]:
                res.append(n)
            else:
                l = 0
                r = len(res)-1
                flag = True
                while l <= r:
                    mid = (l + r) / 2    
                    if res[mid] > n:
                        r = mid - 1
                    elif res[mid] < n:
                        l = mid + 1
                    else:
                        flag = False
                        break
                if flag:
                    res[l] = n
        return len(res)-1
