# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while True:
        	now = (l+r)/2
        	t = guess(now)
        	if t==0:
        		break
        	elif t == 1:
        		l=now+1
        	else:
        		r=now-1
        return now