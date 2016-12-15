class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        data = [[0 for i in range(n + 1)]for j in range(m + 1)]
        for s in strs:
            zeroc = s.count('0')
            onec = len(s) - zeroc
            for i in range(m, zeroc - 1, -1):
                for j in range(n, onec - 1, -1):
                    data[i][j] = max(data[i][j], data[i - zeroc][j - onec] + 1)
        return data[m][n]
