class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        res = [-sys.maxint]
        for t, n in envelopes:
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
