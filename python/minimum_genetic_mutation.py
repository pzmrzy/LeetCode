import Queue
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        wordList, beginWord, endWord = set(bank), start, end
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
                        return dis
                    q.put((v, dis + 1))
        return -1
        
