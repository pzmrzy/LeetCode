class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n1 = ['0', '1', '8']
        n2 = ['11', '88', '69', '96', '00']
        if n == 1:
            return n1
        if n == 2:
            return n2[:-1]
        mid = (n - 1) / 2
        if n % 2 == 0:
            return [p[:mid] + c + p[mid:] for c in n2 for p in self.findStrobogrammatic(n - 2)]
        else:
            return [p[:mid] + c + p[mid:] for c in n1 for p in self.findStrobogrammatic(n - 1)]
