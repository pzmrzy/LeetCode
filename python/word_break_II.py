class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.dic = {}
        if len(wordDict) == 0:
            return []
        return self.dfs(s, wordDict)
    
    def dfs(self, s, wordDict):
        if s in self.dic:
            return self.dic[s]
        res = []
        if len(s) == 0:
            res.append("")
            return res
        for word in wordDict:
            l = len(word)
            if (s[:l] == word):
                sublist = self.wordBreak(s[l:], wordDict)
                for sub in sublist:
                    res.append(word + ("" if len(sub) == 0 else " ") + sub)
        self.dic[s] = res
        return res
