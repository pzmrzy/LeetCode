class ValidWordAbbr(object):
    def toabb(self, s):
        l = len(s)
        if l <= 2:
            return s
        else:
            return s[0] + str(l - 2) + s[-1]
        
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for word in dictionary:
            abb = self.toabb(word)
            self.dic.setdefault(abb, set())
            self.dic[abb].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = self.toabb(word)
        s = self.dic.get(abb, set())
        if s == set() or (len(s) == 1 and word in s):
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
