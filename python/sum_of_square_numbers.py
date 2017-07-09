class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(math.sqrt(c)) + 1):
            if math.floor(math.sqrt(c - i * i)) == math.sqrt(c - i * i):
                return True
        return False
