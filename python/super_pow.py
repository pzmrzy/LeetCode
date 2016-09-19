ass Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        M = 1337
        tmp = [1]
        for i in range(9):
            tmp.append(tmp[i] * a % M)
        res = tmp[b[0]]
        for c in b[1:]:
            res = res * res % M
            t = res
            res = res * res % M
            res = res * res % M
            res = res * t % M
            res = res * tmp[c] % M
        return res
