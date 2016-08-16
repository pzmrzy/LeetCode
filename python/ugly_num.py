class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0:
            return False
        prime = [2,3,5]
        for p in prime:
            while num % p == 0:
                num /= p
        return num == 1
