class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = True
        head = 1
        step = 1
        while n > 1:
            if flag or n % 2 == 1:
                head += step
            step *= 2
            n /= 2
            flag = not flag
        return head
