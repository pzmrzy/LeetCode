class Solution(object):
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path+[s[:i]], res)
                
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
