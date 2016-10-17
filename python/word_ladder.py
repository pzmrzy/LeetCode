import time
import Queue
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.union(beginWord)
        wordList.union(endWord)
        l = len(beginWord)
        d = {}
        dic = {}
        for word in wordList:
            dic[word] = []
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                d[s] = d.get(s, []) + [word]

        q = Queue.Queue()
        q.put((beginWord, 1))
        close = {}
        while not q.empty():
            now, dis = q.get()
            if now in close:
                continue
            close[now] = True
            for i in range(l):
                tmp = now[:i] + '_' + now[i + 1:]
                neb = d.get(tmp, [])
                for v in neb:
                    if v in close:
                        continue
                    if v == endWord:
                        return dis + 1
                    q.put((v, dis + 1))
        return 0
