class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        l1 = len(word1)
        l2 = len(word2)
        data = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1+1):
            data[i][0] = i
        for i in range(l2+1):
            data[0][i] = i
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    data[i][j] = data[i - 1][j - 1]
                else:
                    data[i][j] = min(data[i - 1][j - 1], data[i - 1][j], data[i][j - 1]) + 1
        return data[l1][l2]
