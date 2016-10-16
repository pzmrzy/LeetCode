class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        try:
            for i in range(n):
                s = words[i]
                l = len(s)
                tmp = ""
                for j in range(l):
                    tmp += words[j][i]
                if s != tmp:
                    return False
        except:
            return False
        return True
