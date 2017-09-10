class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for i in range(len(word)):
                tmp = word[:i] + '_' + word[i + 1:]
                self.dic[tmp].add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            tmp = word[:i] + '_' + word[i + 1:]
            if tmp in self.dic:
                if word not in self.dic[tmp] or len(self.dic[tmp]) > 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
