class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = [i+1 for i in range(n)]
        x = reduce(lambda x, y: x*y, l)
        k -= 1
        res = []        
        for i in range(n, 0, -1):
	        x /= i
	        res.append(l[k / x])
	        del l[k / x]
	        k %= x
        return "".join(map(str, res))
