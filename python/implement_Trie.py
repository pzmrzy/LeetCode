from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.letter = defaultdict(TrieNode)
        self.word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        now = self.root
        for c in word:
            now = now.letter[c]
        now.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        now = self.root
        for c in word:
            now = now.letter.get(c)
            if now is None:
                return False
        return now.word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        now = self.root
        for c in prefix:
            now = now.letter.get(c)
            if now is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
