class Solution(object):
    def dfs(self, word, pos, tmp, count, res):
        if len(word) == pos:
            res.append(tmp + (str(count) if count > 0 else ""))
        else:
            self.dfs(word, pos + 1, tmp, count + 1, res)
            self.dfs(word, pos + 1, tmp + (str(count) if count > 0 else "") + word[pos], 0, res)
        
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs(word, 0, "", 0, res)
        return res
