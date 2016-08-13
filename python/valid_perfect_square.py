class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        l = 2
        r = num
        while True:
            mid = (l + r) / 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
            if l > r:
                return False
