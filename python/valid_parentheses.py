import Queue
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        dic = {'(':')', '[':']', '{':'}'}
        q = Queue.LifoQueue()
        for c in s:
            if c in left:
                q.put(c)
            else:
                if q.empty():
                    return False
                t = q.get()
                if dic[t] != c:
                    return False
        return q.empty()
