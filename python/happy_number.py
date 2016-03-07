class Solution(object):
    def sq(self, n):
        nn = str(n)
        tmp = 0
        for c in nn:
            tmp += int(c) * int (c)
        return tmp
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        l.append(n)
        while True:
            tmp = self.sq(n)
            if (tmp == 1):
                return True
            if (tmp in l):
                return False
            l.append(tmp)
            n = tmp
