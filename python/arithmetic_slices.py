class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        res = 0
        i = 2
        while i < n:
            diff = A[i] - A[i - 1]
            if not diff == A[i - 1] - A[i - 2]:
                i += 1
                continue
            cur = 3
            tmp = 1
            i += 1
            while i < n and A[i] - A[i - 1] == diff:
                cur += 1
                tmp += cur - 2
                i += 1
            res += tmp
        return res
