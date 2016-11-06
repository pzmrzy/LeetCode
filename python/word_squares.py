from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.letter = defaultdict(TrieNode)
        self.word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        now = self.root
        for c in word:
            now = now.letter[c]
        now.word = True

    def getPrefix(self, prefix, n):
        now = self.root
        ret = []
        for c in prefix:
            now = now.letter.get(c)
            if now is None:
                return []

        q = [(now, prefix)]
        res = []
        while len(q) > 0:
            node, s = q[0]
            del q[0]
            if len(s) == n:
                res.append(s)
                continue
            for v in node.letter:
                tv = node.letter.get(v)
                q.append((tv, s+v))
        return res

class Solution(object):
    def dfs(self, Tree, square, words, level, length, res):
        if level == length:
            tres = []
            for row in square:
                tres.append(''.join(row))
            res.append(tres)
            return

        for w in Tree.getPrefix(''.join(square[level][0: level]), length):
            for i in range(level, length):
                square[i][level] = w[i]
                square[level][i] = w[i]
            self.dfs(Tree, square, words, level + 1, length, res)

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        Tree = Trie()
        for w in words:
            Tree.insert(w)
        n = len(words[0])
        square = [['' for i in range(n)] for j in range(n)]
        res = []
        for w in words:
            for i in range(n):
                square[i][0] = w[i]
                square[0][i] = w[i]
            self.dfs(Tree, square, words, 1, n, res)
        return res
