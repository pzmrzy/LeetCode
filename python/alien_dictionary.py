class Solution(object):
    def build(self, w1, w2):
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                return ord(w1[i]) - 97, ord(w2[i]) - 97
        if len(w1) > len(w2):
            return '#', None
        return None, None

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        inbound = [-1 for i in range(26)]
        dic = {}
        for i in range(26):
            dic[i] = []
        for w in words:
            for c in w:
                if inbound[ord(c) - 97] == -1:
                    inbound[ord(c) - 97] = 0
                        
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                continue
            x, y = self.build(words[i], words[i + 1])
            if x == '#':
                return ""
            if x != None:
                if inbound[x] == -1:
                    inbound[x] = 0
                if inbound[y] == -1:
                    inbound[y] = 0
                inbound[y] += 1
                dic[x].append(y)
        res = ""
        # tot = 26 - inbound.count(-10)
        while True:
            try:
                t = inbound.index(0)
                for m in dic[t]:
                    inbound[m] -= 1
                inbound[t] = -1
                res += chr(t + 97)
            except:
                if sum([i for i in inbound if i > 0]) == 0:
                    return res
                else:
                    return ""
