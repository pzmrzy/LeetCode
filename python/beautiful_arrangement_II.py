class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        tmp = range(1, k + 2)
        l, r = 0, k
        flag = True
        while l <= r:
            if flag:
                res.append(tmp[l])
                l += 1
            else:
                res.append(tmp[r])
                r -= 1
            flag = not flag
        res.extend(range(k + 2, n + 1))
        return res
