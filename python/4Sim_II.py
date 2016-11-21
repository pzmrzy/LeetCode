class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        l = len(A)
        dic1 = {}
        for i in range(l):
            for j in range(l):
                t = A[i] + B[j]
                dic1.setdefault(t, 0)
                dic1[t] += 1
        dic2 = {}
        for i in range(l):
            for j in range(l):
                t = C[i] + D[j]
                dic2.setdefault(t, 0)
                dic2[t] += 1
        res = 0
        for key in dic1:
            if -key in dic2:
                res += dic1[key] * dic2[-key]
        return res
        
