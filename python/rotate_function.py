class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        suma = sum(A)
        l = len(A)
        fi_1 = 0
        for i in range(l):
            fi_1 += i * A[i]
        res = fi_1
        for i in range(1, l):
            fi = fi_1 + suma - l * A[l - i]
            if res < fi:
                res = fi
            fi_1 = fi
        return res
