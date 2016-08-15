class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        a = [0, 10, 81]
        tmp = 8
        for i in range(n-2):
            a.append(a[-1] * tmp)
            tmp -= 1
        return sum(a[:n+1])
