import Queue
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        q = Queue.Queue()
        q.put( ("", 0, 0) )
        while not q.empty():
            pat, l, r = q.get()
            if l + r == n*2:
                res.append(pat)
            if l < n:
                q.put( (pat + '(', l + 1, r) )
            if l > r:
                q.put( (pat + ')', l, r + 1) )
        return res
