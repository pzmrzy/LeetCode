class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        l = len(s)
        now = 0
        while now < l:
            ind = s.find('#', now)
            num = int(s[now:ind])
            ts = s[ind + 1: ind + num + 1]
            res.append(ts)
            now = ind + num + 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
