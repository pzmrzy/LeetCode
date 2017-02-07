class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {'q':0, 'w':0, 'e':0, 'r':0, 't':0, 'y':0, 'u':0, 'i':0, 'o':0, 'p':0, 
            'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 'j':1, 'k':1, 'l':1,
            'z':2, 'x':2, 'c':2, 'v':2, 'b':2, 'n':2, 'm':2}
        res = []
        for w in words:
            t = w.lower()
            if all([dic[c] == dic[t[0]] for c in t]):
                res.append(w)
        return res
